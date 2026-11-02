#!/usr/bin/env python3
"""Build a disposable Codex view, keeping Claude sources as the single truth."""
import argparse
import json
import os
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]


def build(root):
    source = root / '.claude/skills'
    dest = root / '.agents/skills'
    dest.mkdir(parents=True, exist_ok=True)
    previous = root / '.codex/generated-files.json'
    owned = set(json.loads(previous.read_text())) if previous.exists() else set()
    outputs = set()

    def emit(path, text=None, target=None):
        rel = str(path.relative_to(root))
        if path.exists() or path.is_symlink():
            if rel not in owned:
                raise RuntimeError(f'Refusing to overwrite unowned file: {path}')
            path.unlink()
        path.parent.mkdir(parents=True, exist_ok=True)
        if target is not None:
            path.symlink_to(os.path.relpath(target, path.parent))
        else:
            path.write_text(text)
        outputs.add(rel)

    for src in sorted(source.rglob('*')):
        if not src.is_file() or '__pycache__' in src.parts or src.suffix == '.pyc':
            continue
        rel = src.relative_to(source)
        out = dest / rel
        if src.suffix != '.md':
            emit(out, target=src)
            continue
        body = src.read_text()
        body = body.replace('.claude/skills/', '.agents/skills/')
        body = body.replace('../../../CLAUDE.md', '../../../AGENTS.md')
        if rel.parts[0] != 'nature-figure':
            body = body.replace('mcp__codex__codex-reply', 'mcp__claude_reviewer__review_reply')
            body = body.replace('mcp__codex__codex', 'mcp__claude_reviewer__review')
        # Translate the concrete new-review examples to the bridge schema.
        if rel.parts[0] != 'nature-figure':
            body = re.sub(r'  model: \$REVIEWER_MODEL\n  config: \{"model_reasoning_effort": "\$REVIEWER_EFFORT_(DEEP|REGULAR)"\}\n',
                          lambda m: '  executor_model: <actual executor model ID>\n  tier: ' + m[1].lower() + '\n  cwd: <absolute project directory>\n', body)
        if str(rel) == 'research-review/SKILL.md':
            body = body.replace('a Claude sub-agent audits', 'a Codex sub-agent audits').replace('while Codex reviews only', 'while Claude reviews only')
            body = body.replace('backend (Codex or manual)', 'backend (Claude or manual)')
            body = re.sub(r'## Constants.*?## Context:', '## Reviewer transport\n\nUse [Codex reviewer routing](../shared-references/reviewer-routing.md).\nDefault backend: Claude; manual review remains an explicit override.\nFor manual calls preserve the identity-bearing config and primary inputs.\n\n## Context:', body, flags=re.S)
            body = re.sub(r'## Prerequisites.*?## Full project review', '## Prerequisites\n\nRun `bash install.sh --host codex` and load the project MCP servers.\n\n## Full project review', body, flags=re.S)
            body = body.replace('For codex backend:', 'For claude backend:').replace('`codex` backend', '`claude` backend')
            body = re.sub(r'- ALWAYS pin .*?\n- That pin .*?\n', '- The Claude bridge pins model and effort from host configuration; pass the deep tier.\n', body)
        if str(rel) == 'shared-references/reviewer-routing.md':
            body = (root / 'config/codex/reviewer-routing.md').read_text()
        if str(rel) == 'nature-figure/references/imagegen-generation.md':
            body = (root / 'config/codex/imagegen-generation.md').read_text()
        if str(rel) == 'shared-references/split-review.md':
            body = body.replace('Claude sub-agent', 'Codex sub-agent').replace('paper review (Codex)', 'paper review (Claude)')
        if str(rel) == 'research-agent-team/SKILL.md':
            body = re.sub(r'In Claude Code, delegate with the Agent tool.*?Codex route\.',
                          'On Codex, follow the delegation section in [host contract](../shared-references/codex-host.md). Read role definitions as task instructions, use actual spawn and follow-up tools, and pass fresh context for independent checks. Role QA is same-family; external review uses Claude.', body, flags=re.S)
            body = re.sub(r'The user may select an option or correct its premise\. In Claude Code,.*?Silence or a dismissed question is not approval\.',
                          'The user may select an option or correct its premise. Use the actual input tools under the [host contract](../shared-references/codex-host.md). Continue unaffected work while an asynchronous question is pending. Automatic selection only applies to cards already authorized for it; record the selected option and source. Topic approval always waits for an explicit reply after the Chinese topic report. Silence or dismissal is not approval.', body, flags=re.S)
            body = re.sub(r'In Claude Code, a Bash\ncommand.*?starts it again\.',
                          'On Codex, track running process IDs and poll with the available wait tools. A background process does not automatically resume the agent after the session ends.', body, flags=re.S)
        if str(rel) == 'shared-references/split-review.md':
            body = body.replace('`config: {"model_reasoning_effort": "max"}`', '`tier: deep`, `executor_model: <actual model>`')
            body = body.replace('`sandbox: read-only`, cwd', 'read-only bridge, cwd')
        if str(rel) == 'paper-polish/SKILL.md':
            body = body.replace('## Overview', '## Default executor\n\nCodex performs this language pass directly. Gemini is an explicit opt-in only.\n\n## Overview')
            body = body.replace('Claude keeps content and evidence', 'Codex keeps content and evidence')
        if src.name == 'SKILL.md':
            match = re.match(r'---\n(.*?)\n---\n', body, re.S)
            if not match:
                raise RuntimeError(f'Missing frontmatter: {src}')
            front = match.group(1)
            explicit = 'disable-model-invocation: true' in front
            front = re.sub(r'^(allowed-tools|disable-model-invocation|argument-hint):.*\n?', '', front, flags=re.M)
            extra = re.findall(r'^(?:author|version|tags|dependencies):.*$', front, re.M)
            if extra:
                front = re.sub(r'^(?:author|version|tags|dependencies):.*\n?', '', front, flags=re.M)
                # Source metadata is retained as strings under the portable field.
                front += '\nmetadata:\n' + '\n'.join(
                    '  ' + line.split(':', 1)[0] + ': ' + json.dumps(line.split(':', 1)[1].strip())
                    for line in extra)
            body = '---\n' + front.rstrip() + '\n---\n\n' + (
                '**Codex host:** First read [host contract](../shared-references/codex-host.md). '
                'It overrides host/tool/model examples below; research policies remain unchanged.\n\n'
            ) + body[match.end():]
            if explicit:
                emit(out.parent / 'agents/openai.yaml', 'policy:\n  allow_implicit_invocation: false\n')
        emit(out, body)
    emit(dest / 'shared-references/codex-host.md', (root / 'config/codex/host.md').read_text())
    emit(dest / 'research-auto/SKILL.md', '''---
name: research-auto
description: Explicitly activate the existing automatic research workflow for this task.
---
Read ../shared-references/codex-host.md and ../research-agent-team/SKILL.md.
The user's explicit invocation activates automatic mode for this task. Follow the
existing full-flow rules and stop for explicit human approval after topic selection.
''')
    emit(dest / 'research-auto/agents/openai.yaml', 'policy:\n  allow_implicit_invocation: false\n')
    emit(dest / 'research-autopilot/SKILL.md', '''---
name: research-autopilot
description: Explicitly activate post-topic autopilot for this task; after topic approval the agent decides all research choices and asks the user only for missing resources.
---
Read ../shared-references/codex-host.md and ../research-agent-team/SKILL.md.
The user's explicit invocation activates automatic mode in its post-topic autopilot
variant for this task. Follow the controller's "Post-topic autopilot" rules: stop for
explicit human approval after topic selection, then decide research choices yourself
and request missing resources from the user as soon as they arise.
''')
    emit(dest / 'research-autopilot/agents/openai.yaml', 'policy:\n  allow_implicit_invocation: false\n')
    for rel in owned - outputs:
        path = root / rel
        if path.is_relative_to(dest) and (path.is_file() or path.is_symlink()):
            path.unlink()
    previous.parent.mkdir(exist_ok=True)
    previous.write_text(json.dumps(sorted(outputs), indent=2) + '\n')
    print(f'Generated {len(list(dest.glob("*/SKILL.md")))} Codex skills in {dest}')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', type=Path, default=ROOT)
    build(parser.parse_args().root.resolve())
