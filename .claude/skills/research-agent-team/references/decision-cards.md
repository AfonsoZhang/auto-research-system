# Decisions in automatic mode

The main agent uses the full task context to select and execute ordinary choices
within the user's existing delegated authority. No separate model or decision MCP
is required. A card records the decision; it is not a mandatory user interruption.

For a material delegated choice, record in the existing task record:
- The question and feasible options (normally two or three).
- The selected option and the evidence and rationale supporting it.
- Relevant uncertainty, authorization, budget and affected downstream work.
- Decision source (`main_agent`, `main_agent (autopilot)` or `user`) and the actual outcome when known.

Do not invent calibrated probabilities, success rates or model confidence scores.
Inspect original artifacts; a recommendation is neither research evidence nor an
independent review verdict. Keep the separate external-review and acceptance rules.

When evidence is insufficient, choose an authorized, bounded, reversible check
that can distinguish the options. Otherwise complete independent work and report
the missing input. Do not spend beyond the agreed cap or retry indefinitely.

Topic approval is always a human checkpoint: record `AWAITING_TOPIC_APPROVAL`,
report the proposed topic/version and wait for an explicit reply before dependent
work. If using a structured card, mark `decision_kind: "topic_approval"` and
`delegated: false`, with no automatic default. Existing approval for the same topic
and scope remains valid. New authority and final academic commitments stay with
the user; silence or a timeout cannot authorize them.

In post-topic autopilot, the main agent also decides material claim or direction
changes within the approved topic; record them with
`decision_source: "main_agent (autopilot)"`. Resource requests are not cards for
automatic selection: follow the controller's
[autopilot rules](../SKILL.md#post-topic-autopilot).

User replies override unfinished decisions. Record work already executed accurately.
In on-demand mode, finish the requested scope; these rules do not activate automatic
mode or authorize a further stage.
