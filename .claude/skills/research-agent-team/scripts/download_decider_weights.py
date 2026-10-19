#!/usr/bin/env python3
"""Resume the authorized local weight install when Hugging Face is reachable."""
import hashlib
import json
import os
from pathlib import Path
import re
import shutil
import tempfile
import urllib.request

ROOT = Path(os.environ.get('RESEARCH_ROOT') or Path(__file__).resolve().parents[4])
RUNTIME = ROOT / '.tools/clarification-decider'
# Override with DECIDER_WEIGHTS_REPO / DECIDER_WEIGHTS_FILE to use another GGUF model.
REPO = os.environ.get('DECIDER_WEIGHTS_REPO', 'manjunathshiva/opendecider-small-GGUF')
FILENAME = os.environ.get('DECIDER_WEIGHTS_FILE', 'opendecider-small-q4_k_m.gguf')


def sha256(path):
    digest = hashlib.sha256()
    with path.open('rb') as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b''):
            digest.update(chunk)
    return digest.hexdigest()


def main():
    with urllib.request.urlopen(f'https://huggingface.co/api/models/{REPO}?blobs=true', timeout=30) as response:
        meta = json.load(response)
    revision = meta['sha']
    file_meta = next(item for item in meta['siblings'] if item['rfilename'] == FILENAME)
    expected = file_meta['lfs']['sha256']
    if not re.fullmatch(r'[a-f0-9]{40}', revision) or not re.fullmatch(r'[a-f0-9]{64}', expected):
        raise ValueError('Missing valid repository revision / weight SHA-256')
    target = RUNTIME / 'models' / FILENAME
    target.parent.mkdir(parents=True, exist_ok=True)
    if target.exists():
        if sha256(target) != expected:
            raise FileExistsError('Existing model differs; inspect it before replacing it')
    else:
        url = f'https://huggingface.co/{REPO}/resolve/{revision}/{FILENAME}'
        # Only public model bytes are downloaded; no credentials or research content are sent.
        with tempfile.NamedTemporaryFile(dir=target.parent, prefix='.download-', delete=False) as temp:
            temporary = Path(temp.name)
            try:
                with urllib.request.urlopen(url, timeout=60) as response:
                    shutil.copyfileobj(response, temp, length=1024 * 1024)
                temp.flush()
                if sha256(temporary) != expected:
                    raise ValueError('Downloaded weight SHA-256 does not match the official manifest')
            except BaseException:
                temporary.unlink(missing_ok=True)
                raise
        temporary.replace(target)
    config_path = RUNTIME / 'config.json'
    config = json.loads(config_path.read_text())
    with tempfile.NamedTemporaryFile(prefix='clarification-decider-config-', suffix='.json', dir=RUNTIME, delete=False) as backup:
        backup.write(config_path.read_bytes())
        print('Configuration backup:', backup.name)
    config.update(model_path=str(target), model_revision=revision, model_sha256=expected,
                  automatic_selection=False, validation_state='weights_ready_card_evaluation_pending')
    config.pop('network_error', None)
    with tempfile.NamedTemporaryFile(mode='w', dir=RUNTIME, prefix='.config-', delete=False) as temp:
        json.dump(config, temp, ensure_ascii=False, indent=2)
        temp.write('\n')
        pending = Path(temp.name)
    pending.replace(config_path)
    print('Weights verified; run actual card evaluations before enabling automatic selection.')


if __name__ == '__main__':
    main()
