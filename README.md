# Auto-Research System

A set of agent skills, shared research policies and a research controller for
running research with Claude Code or Codex: topic selection, literature and
novelty checks, experiment planning and execution, result analysis, paper
planning and writing, figures, review and rebuttal. Version 1.0.

It is not tied to one model vendor or relay. The executor is whichever agent
you run (Claude Code or Codex); the decision model, image provider and external
reviewer are each chosen in local configuration.

## What is included

| Part | Where |
|---|---|
| 37 skills (Claude and Codex share one copy) | `.agents/skills/`, linked from `.claude/skills/` |
| Shared research policies: claim preservation, contribution-type routing, target-venue calibration, topic selection, publication/version policy, research autonomy | `.agents/skills/shared-references/` |
| Research controller and automatic mode | `.agents/skills/research-agent-team/` |
| Decision-card tool (MCP `choose_card`) | `research-agent-team/scripts/clarification_decider.py` |
| Specialist agents for automatic mode | `.claude/agents/`, `.codex/agents/` |
| Literature helpers (arXiv, OpenAlex, Semantic Scholar, Exa) | `.agents/aris/tools/` |
| Codex reviewer bridge (MCP) | `.agents/mcp-servers/codex-exec/` |
| Routing rules loaded by both runtimes | `AGENTS.md` (Claude loads it via `CLAUDE.md`) |

## Install

```bash
git clone <this repository> research && cd research
./install.sh                 # WITH_DIAGRAMS=1 ./install.sh also sets up diagram rendering
```

`install.sh` creates local, untracked configuration under `.tools/` from
`config/*.example.json`, renders `.mcp.json` and `.codex/config.toml`, and
installs the decision-card client. It downloads no model weights. Requirements:
Python 3.10+, Node 18+ for image generation, and Claude Code or Codex CLI.

## Configure (all optional)

| Component | File | Choices | When unconfigured |
|---|---|---|---|
| Decision model for automatic-mode cards | `.tools/clarification-decider/config.json` | Any OpenAI-compatible server returning `top_logprobs` (vLLM, LM Studio, Ollama, llama.cpp, a hosted gateway), or a local GGUF run on demand | The main agent decides under its existing authorization |
| Image generation | `.tools/image-provider.json` | Any OpenAI-compatible chat endpoint that returns images; adapters for Poe and OpenRouter | Prompts are planned; generation is reported as unavailable |
| External reviewer | `.tools/reviewer.json` | Codex MCP with whatever provider your Codex CLI uses, or a manual reviewer | External review is reported as unavailable, never replaced by self-review |
| Literature APIs | environment variables | `EXA_API_KEY`, `SEMANTIC_SCHOLAR_API_KEY`, `OPENALEX_EMAIL` | Keyless sources are used and coverage gaps are reported |

Keys are always read from environment variables named in the configuration.
Set `RESEARCH_ROOT` to the repository path if you run helper scripts by hand.
A decision model must be validated on your own cards before you set
`automatic_selection: true`.

## How it behaves

- **One request, one scope.** A skill finishes the requested work and its
  necessary checks; a "next step" in a skill is not permission to continue.
- **Automatic mode** runs the full flow only when you explicitly turn it on for
  a task. Ordinary clarification cards may then be decided by the configured
  decision model or the main agent.
- **Human checkpoints.** Approval of a newly selected topic always waits for you;
  no timeout, default or model can release it. Spending beyond an authorized
  budget, renting compute, pushing code and outward-facing actions also need you.
- **Evidence integrity.** Pre-registered criteria are not changed after results
  are seen without disclosure; failed pilots stop downstream spending; claims are
  kept at the strength the evidence supports.

## Status and limits

- Tested: decision-card contract (14 offline tests), image adapters (13), nature-response
  (7) and nature-shared (5) package checks. Most skills are instruction files without
  automated behavioural tests.
- The decision model has been checked only on 12 synthetic English cards; this
  shows the integration works, not that its research decisions are accurate.
- Venue rules, deadlines and rankings must be re-verified against official pages.

## License

CC BY-NC-SA 4.0 (`LICENSE`): you may share and adapt this work for
non-commercial purposes with attribution, under the same license. Components
adapted from other projects keep their original notices; see
`THIRD_PARTY_NOTICES.md`.
