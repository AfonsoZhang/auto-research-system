# Research project routing (Claude Code)

- **Default: standalone skills and scoped revisions.** Existing skills remain directly
  callable at the root and in child projects. Complete the current request and necessary
  verification without automatically starting a team or the next stage. For revisions,
  read existing artifacts and edit the requested scope; do not restart research.
- **Shared standards, loaded by impact.** Root and child-project work follows the
  [shared research policy](.claude/skills/shared-references/research-autonomy.md#local-changes).
  Load relevant clauses, verify affected dependencies, and reuse valid checks.
- **Working language.** Apply the shared [language policy](.claude/skills/shared-references/research-autonomy.md#working-language):
  English internal instructions and work; Chinese final and topic-approval reports.
- **Research controller.** For root-level research coordination, stage assessment or
  cross-stage management, read [research-agent-team](.claude/skills/research-agent-team/SKILL.md).
  One main agent coordinates stages, specialist skills, execution and acceptance within
  the current request. Existing specialist skills remain directly callable.
- **Automatic mode.** Enable team assignments, authorized card selection and continuous
  execution only when the user explicitly activates automatic mode for this task
  (typing `/research-auto` counts as explicit activation).
  The controller defines completion and stopping conditions. Discussing or editing it,
  entering the directory, high reasoning effort, silence or past activation is not activation.
- **Human checkpoint after topic selection.** After fresh selection or reselection,
  follow the [topic-approval rule](.claude/skills/shared-references/topic-selection-policy.md#human-approval-after-topic-selection)
  and wait for the user's explicit decision. Automatic mode, timed defaults and decision
  recommendations cannot supply approval.
- **Child projects retain their existing workflow.** Ordinary child-project sessions do
  not inherit root team execution. A root task already in automatic mode may delegate
  scoped work there without changing the child's default workflow.
- **Single-call boundary.** Next-step and handoff suggestions do not authorize execution.
  Execute multiple stages only within an explicitly requested workflow. Complete necessary
  verification, self-checks, compilation and figure checks without expanding the task.
- `$RESEARCH_ROOT` denotes this file's directory. Substitute that path before running
  commands if the environment variable is unset.
- Preserve more specific child-project revision, freeze and data constraints.
  This routing applies only to `$RESEARCH_ROOT`.
- **Standing authorization: citation verification sub-agent.** When
  `paper-writer` requires an independent citation check (full paper, Final mode, or three
  or more citations; also via `intro-drafter`), dispatch one fresh-context sub-agent for
  that check without asking again. This covers only that verification step, not other
  sub-agent use.
