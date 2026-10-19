#!/usr/bin/env python3
"""One MCP tool for research clarification cards; never executes an option."""
from __future__ import annotations

import argparse
import contextlib
import fcntl
import hashlib
import json
import math
import os
from pathlib import Path
import socket
import subprocess
import tempfile
import time
import urllib.request

ROOT = Path(os.environ.get('RESEARCH_ROOT') or Path(__file__).resolve().parents[4])
DEFAULT_CONFIG = Path(os.environ.get('DECIDER_CONFIG')
                      or ROOT / '.tools/clarification-decider/config.json')


def choose(card: dict, infer, *, automatic=False, model_name='unavailable') -> dict:
    """Validate a card before inference. Authority is supplied by the main agent."""
    if not isinstance(card, dict):
        raise ValueError('card must be an object')
    digest = hashlib.sha256(json.dumps(card, ensure_ascii=False, sort_keys=True,
                                     allow_nan=False).encode()).hexdigest()
    result = {'card_id': card.get('card_id'), 'input_sha256': digest,
              'status': 'main_agent_required', 'choice': None, 'source': 'none',
              'model': model_name, 'action_executed': False}
    for key in ('card_id', 'question', 'background'):
        if not isinstance(card.get(key), str) or not card[key].strip():
            raise ValueError(f'{key} must be a nonempty string')
    options = card.get('options')
    if not isinstance(options, dict) or not 2 <= len(options) <= 3:
        raise ValueError('options must contain 2–3 ID-to-description entries')
    if any(not isinstance(k, str) or not k.strip() or not isinstance(v, str)
           or not v.strip() for k, v in options.items()):
        raise ValueError('option IDs and descriptions must be nonempty strings')
    allowed = card.get('authorized_option_ids', [])
    if not isinstance(allowed, list) or any(k not in options for k in allowed):
        raise ValueError('authorized_option_ids must be a list of option IDs')
    if card.get('user_choice') is not None:
        selected = card['user_choice']
        if selected not in options:
            raise ValueError('user_choice is not one of the options; revise the card')
        result.update(source='user', choice=selected,
                      status='selected' if selected in allowed else 'user_required',
                      reason='explicit_user_choice' if selected in allowed else 'authorization_or_resource_needed')
        return result
    # Topic selection is a human checkpoint even under general unattended delegation.
    if card.get('decision_kind') == 'topic_approval':
        result.update(status='user_required', reason='topic_approval_requires_user')
        return result
    if card.get('delegated') is not True or not allowed:
        result.update(status='user_required', reason='no_delegated_authorized_options')
        return result
    for key in ('constraints', 'preferences'):
        value = card.get(key, [])
        if not isinstance(value, list) or any(not isinstance(x, str) for x in value):
            raise ValueError(f'{key} must be a list of strings')
    eligible = {k: v for k, v in options.items() if k in allowed}
    if len(eligible) == 1:
        result.update(status='selected', choice=next(iter(eligible)), source='rule',
                      reason='only_authorized_option')
        return result
    # Keep the user's constraints, but do not feed the model the recommended/default ID.
    state = {k: card.get(k, []) if k != 'background' else card[k]
             for k in ('background', 'constraints', 'preferences')}
    try:
        raw = infer(state, card['question'], eligible)
        answer = raw['answers']['card']
        probs = answer['probabilities']
        if set(probs) != set(eligible):
            raise ValueError('probabilities do not match authorized options')
        if any(isinstance(p, bool) or not isinstance(p, (float, int))
               or not math.isfinite(p) or not 0 <= p <= 1 for p in probs.values()):
            raise ValueError('invalid option probabilities')
        if not math.isclose(sum(probs.values()), 1, abs_tol=1e-4):
            raise ValueError('probabilities do not sum to one')
        selected = answer['choice']
        if selected not in eligible or probs[selected] != max(probs.values()):
            raise ValueError('invalid selected option')
        result.update(source='model', suggested_choice=selected, probabilities=probs,
                      model_response=raw)
        if raw.get('warnings') or answer.get('truncated'):
            result['reason'] = 'model_input_warning'
        elif list(probs.values()).count(max(probs.values())) != 1:
            result['reason'] = 'tied_options'
        elif not automatic:
            result['reason'] = 'local_card_validation_pending'
        elif card.get('execution_mode') != 'unattended_research':
            result['reason'] = 'automatic_selection_outside_unattended_mode'
        else:
            result.update(status='selected', choice=selected, reason='model_choice')
    except Exception as exc:
        # No fabricated decision/probability. The main agent retains the original fallback.
        result.update(reason='model_unavailable_or_invalid', error_type=type(exc).__name__,
                      error=str(exc)[:600])
    return result


@contextlib.contextmanager
def local_engine(cfg: dict, config_path: Path = DEFAULT_CONFIG):
    """Run a local CPU model only for the duration of a card call."""
    binary, weights = Path(cfg['engine_binary']), Path(cfg['model_path'])
    if not binary.is_file() or not weights.is_file():
        raise RuntimeError('Local model is not ready: complete the recorded weights download first')
    # Serialize card calls so multiple MCP clients cannot exhaust local memory.
    lock_path = config_path.parent / 'inference.lock'
    with lock_path.open('a') as lock:
        try:
            fcntl.flock(lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
        except BlockingIOError:
            raise RuntimeError('Local decision model is busy; use the main-agent fallback') from None
        with socket.socket() as sock:
            sock.bind(('127.0.0.1', 0))
            port = sock.getsockname()[1]
        url = f'http://127.0.0.1:{port}'
        command = [str(binary), '-m', str(weights), '--host', '127.0.0.1', '--port', str(port),
                   '--alias', served_model(cfg), '-c', '2048', '-t', str(cfg.get('threads', 2)),
                   '-ngl', '0', '-np', '1', '--jinja']
        with tempfile.TemporaryFile() as err:
            proc = subprocess.Popen(command, stdout=subprocess.DEVNULL, stderr=err)
            try:
                deadline = time.monotonic() + 45
                while True:
                    if proc.poll() is not None:
                        raise RuntimeError(f'Local model server exited with status {proc.returncode}')
                    try:
                        with urllib.request.urlopen(url + '/health', timeout=1) as response:
                            if response.status == 200:
                                break
                    except OSError:
                        pass
                    if time.monotonic() >= deadline:
                        raise TimeoutError('Local model startup exceeded 45 seconds')
                    time.sleep(0.2)
                yield url + '/v1'
            finally:
                if proc.poll() is None:
                    proc.terminate()
                    try:
                        proc.wait(timeout=5)
                    except subprocess.TimeoutExpired:
                        proc.kill()
                        proc.wait()


def run_card(card: dict, config_path: Path = DEFAULT_CONFIG) -> dict:
    try:
        cfg = json.loads(config_path.read_text())
    except (OSError, ValueError):
        cfg = {}

    def ask(base_url, api_key, state, question, options):
        from opendecider import load
        model = load(f'openai:{served_model(cfg)}', base_url=base_url, api_key=api_key,
                     timeout=cfg.get('timeout_seconds', 60))
        return model.system_one(state, {'card': {'type': 'choice',
                                'instructions': question, 'criteria': options}})

    def infer(state, question, options):
        backend = cfg.get('backend')
        if backend == 'local_gguf':
            with local_engine(cfg, config_path) as url:
                return ask(url, None, state, question, options)
        if backend == 'openai_compatible':
            # Any server with /v1/chat/completions returning top_logprobs (vLLM, LM Studio,
            # Ollama, llama.cpp, a hosted gateway). The key is read from the named env var.
            if not cfg.get('base_url'):
                raise RuntimeError('openai_compatible backend needs base_url')
            key_env = cfg.get('api_key_env')
            return ask(cfg['base_url'], os.environ.get(key_env) if key_env else None,
                       state, question, options)
        raise RuntimeError('Decision backend is not configured')

    return choose(card, infer, automatic=cfg.get('automatic_selection') is True,
                  model_name=cfg.get('model_id', 'decision model (not configured)'))


def served_model(cfg: dict) -> str:
    return cfg.get('served_model', 'opendecider-small')


def serve(config_path: Path):
    import anyio
    from mcp.server.mcpserver import MCPServer
    from mcp.types import ToolAnnotations

    server = MCPServer(name='research_clarification', version='1.0.0',
                       instructions='Only choose between options on an authorized research clarification card. '
                       'The main agent handles authority, execution and fallback. No research or workflow routing.')

    @server.tool(annotations=ToolAnnotations(read_only_hint=True, destructive_hint=False,
                                             idempotent_hint=True, open_world_hint=False))
    async def choose_card(card: dict) -> dict:
        """Research clarification card only. Required: card_id, question, background,
        options (2–3 ID:description pairs), authorized_option_ids, delegated.
        Optional: constraints, preferences (string lists), user_choice, default_id,
        execution_mode (unattended_research permits automatic model selection when enabled),
        decision_kind (topic_approval always requires an explicit user choice).
        Supply the question, background, options, constraints and preferences in English.
        Returns selected, main_agent_required or user_required; never executes an action.
        """
        return await anyio.to_thread.run_sync(run_card, card, config_path)

    server.run('stdio')


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--config', type=Path, default=DEFAULT_CONFIG)
    ap.add_argument('--card', type=Path, help='Run one JSON card instead of serving MCP')
    args = ap.parse_args()
    if args.card:
        print(json.dumps(run_card(json.loads(args.card.read_text()), args.config), ensure_ascii=False, indent=2))
    else:
        serve(args.config)


if __name__ == '__main__':
    main()
