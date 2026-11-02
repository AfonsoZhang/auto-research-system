---
description: 选题后全自动模式——选题经你批准后，研究方向上的决定全部由 agent 自定、一路推进到交付；只有缺资源（预算/算力/付费服务/数据/权限）时立刻向你汇报索要
argument-hint: [可选：本次任务与终点；留空则推进到完整论文交付]
disable-model-invocation: true
---

The user typed `/research-autopilot`. This invocation **is** the explicit activation of
automatic mode required by `$RESEARCH_ROOT/CLAUDE.md`, in its **post-topic autopilot**
variant, scoped to **this task only**. It does not carry over to later tasks or sessions.

Task and endpoint from the user: $ARGUMENTS

# What differs from `/research-auto`

Everything in [`/research-auto`](research-auto.md) applies, including its step order,
announcement and limits, with two changes. The controller's
[autopilot rules](../skills/research-agent-team/SKILL.md#post-topic-autopilot) are the
source of truth.

1. **Research decisions are delegated.** Once the topic is approved, the main agent
   decides every research question itself: experiment design, branch cuts, pivots after
   a scientific stop or inconclusive pilot, and material changes to the central claim or
   paper direction within the approved topic. Record each such decision under the
   [decision-card policy](../skills/research-agent-team/references/decision-cards.md)
   with `decision_source: "main_agent (autopilot)"`; do not ask the user.
2. **Missing resources are requested at once.** The moment work needs a resource the
   task is not authorized to use, post a Chinese `资源请求` block in the progress
   message (what, why, amount/cost, what it unblocks, the fallback if refused), record it
   as `AWAITING_RESOURCE` in the tracker, and keep working on everything that does not
   depend on it. Check for the user's reply before starting dependent work. When only
   blocked work remains, ask with AskUserQuestion (one question per resource) and wait.

# Topic

- No approved topic for this task: run topic selection, deliver the Chinese topic report,
  record `AWAITING_TOPIC_APPROVAL` and end the turn. Autopilot starts at the user's
  explicit approval; no timeout, default or recommendation can approve.
- An approved topic exists: start downstream work immediately.
- Replacing the approved question or contribution type is a new topic and needs a new
  report and approval; everything short of that is the agent's call.

# Still with the user

Resources and authority (spending beyond the agreed budget, paid services, renting
compute, data access, credentials) and outward-facing actions (submission, arXiv, code
or data release, pushing to remotes, sending unpublished text to an external model,
destructive operations). Collect pending outward-facing actions in the final report.
