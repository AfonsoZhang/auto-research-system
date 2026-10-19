# Automatic selection of clarification-card options

For the main agent of a research-root task already in automatic mode. When the user
has authorized automatic selection, send an existing, adequately investigated card
to `mcp__research_clarification__choose_card` (load its schema with ToolSearch when
it is deferred). Ordinary revisions, standalone skill calls
and routine child-project work do not activate it. The tool advises; it does not
execute the selected action.

The main agent marks automatic-mode cards `execution_mode: "unattended_research"`.
This is a compatibility value, not a separate mode. Automatically adopt a valid model
choice only when `automatic_selection` is enabled and the card has that mode marker.
Other modes or missing markers produce advice only. The marker must come from the
current user's delegation, not silence. Configuring a decision model for automatic
mode does not itself launch research.

The [post-selection human checkpoint](../../shared-references/topic-selection-policy.md#human-approval-after-topic-selection)
is excluded from automatic selection, including in automatic mode. Topic approval
cards use `decision_kind: "topic_approval"`, `delegated: false` and no default ID.
Without an actual user choice, the tool returns `user_required` with reason
`topic_approval_requires_user` before inference or any single-option shortcut,
even if a caller incorrectly marks the card delegated. The main agent must wait;
there is no fallback/default decision for this checkpoint. Populate `user_choice`
only from the user's reply to the reported topic/version, recorded in the tracker.

## Inputs and outcomes

Each card has one question, 2–3 options with stable IDs, context, user preferences
and constraints. Identify authorized option IDs, the default and any actual user
answer. The main agent establishes authority from real instructions; the model cannot
create it. Do not call the model to replace approval that remains with the user.

For topic cards, first apply the
[context policy](../../shared-references/topic-context-policy.md#accept-the-choice-and-preserve-its-origin).
Check the options and consequential constraints against the scoped brief and
source evidence. The card model cannot recover omitted alternatives. Distinguish
user requirements from facts, preferences and agent choices in the existing
background/tracker; an ordinary model-selected option remains a delegated decision
after summarization. Such a decision never supplies the required topic approval.

Send questions, context, options, constraints and preferences in English. Faithfully
translate non-English requirements and preserve the original for verification. Do
not drop constraints or add authority in translation. Apply the shared
[working-language policy](../../shared-references/research-autonomy.md#working-language)
to the workflow and its artifacts, including the Chinese user-report exceptions.

Do not feed recommendation/default labels into option descriptions. Give comparable
information about consequences, benefits and costs for every option so selection
can assess the options rather than echo the main agent. Preserve the original card
and identify any translation.

Distinguish `selected`, `main_agent_required` and `user_required`. Adopt an authorized
option only for `selected`; otherwise follow the main agent's existing rules. Do
not invent probabilities or explanations when the model fails or is uncertain.
Keep the main agent's evidence-based rationale separate from the model's actual
choice and probabilities.

Reuse the card or project tracker for the card ID and version/input hash, options,
returned value, model/version, actual decision source (user / model / main_agent),
action and outcome. Check for new user replies before dependent work; explicit
replies take precedence for work not yet executed.

## Local integration

Keep MCP configuration, scripts, documentation and this team skill at the research
root, outside legacy child-project replication. Claude Code registers the server in
`$RESEARCH_ROOT/.mcp.json` (enabled by `enabledMcpjsonServers` in
`.claude/settings.local.json`) and runs this copy's `scripts/clarification_decider.py`;
Restart Claude Code after changing `.mcp.json`. Dependencies live in
`$RESEARCH_ROOT/.venvs/clarification-decider/`; runtime configuration and models live
in `$RESEARCH_ROOT/.tools/clarification-decider/`, outside skill synchronization.

Configuration selects the model/backend without binding the workflow to a provider
(`config.example.json`; override its path with `DECIDER_CONFIG`):

- `backend: "local_gguf"`: start local llama.cpp as needed and load `model_path`.
- `backend: "openai_compatible"`: use an endpoint returning `top_logprobs`, such as
  vLLM, LM Studio, Ollama, llama.cpp or a hosted gateway, with `base_url` and
  `served_model`; read the key from the environment variable named by `api_key_env`.
- Unconfigured: return `main_agent_required`.

Expose only `choose_card`, not upstream task-routing, guard or research-evaluation
tools. After changing models, validate on local English cards before enabling
`automatic_selection`. An unavailable model/interface returns `main_agent_required`;
fallback is not model success.

Model use in automatic mode requires user authorization. If download or inference
is unavailable, the main agent selects within existing authority. Model files and
actual test status are established by `.tools/clarification-decider/config.json`
and its referenced verification records. An installed package or successful MCP
handshake does not prove inference ran. To download weights again, use
`python3 $RESEARCH_ROOT/.claude/skills/research-agent-team/scripts/download_decider_weights.py`.
It pins the official revision for that download and verifies SHA-256; it does not
automatically enable model selection.

Call `mcp__research_clarification__choose_card` with `card={...}`. Card JSON fields are `card_id`,
`question`, `background`, `options` (ID to description), `authorized_option_ids`
and `delegated`. Optional fields are `constraints`, `preferences`, `user_choice`,
`default_id`, `execution_mode` and `decision_kind`; the human topic checkpoint must
use `topic_approval`. `default_id` is not sent to the model. For CLI inspection:
`$RESEARCH_ROOT/.venvs/clarification-decider/bin/python $RESEARCH_ROOT/.claude/skills/research-agent-team/scripts/clarification_decider.py --card <card.json>`.

Validate constraint adherence, response to preferences and option-order stability
on English cards before selecting the scope of automatic adoption. Returned
probabilities are not measured workspace accuracy or publication success rates.
Until local replay validation passes, keep selections advisory and let the main
agent decide. Separate tuning examples from final evaluation. A few synthetic
cards verify integration and basic behavior, not real research-decision accuracy.
