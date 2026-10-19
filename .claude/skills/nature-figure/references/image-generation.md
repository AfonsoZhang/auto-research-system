# Model-generated images: route selection

Use for generated illustrations, scenes, visual assets and explicitly requested
AI graphical abstracts. Data plots and exact labelled diagrams use their own routes.

## Resolve the generation route

Use, in order:

1. An explicit provider/model choice in the current task.
2. The user's local configuration: `IMAGE_PROVIDER_CONFIG`, else
   `$RESEARCH_ROOT/.tools/image-provider.json`.
3. The `imagegen` skill with the built-in `image_gen` tool. This also applies to shared skill copies in
   child projects without a local provider configuration.

A built-in configuration uses `{"provider":"imagegen","mode":"built_in"}`.
Read [imagegen-generation.md](imagegen-generation.md) for the Codex handoff,
tool availability and delivery. It requires neither a Poe balance nor an API key.
Do not invent a model ID, token price or remaining quota for the built-in tool.
Antigravity is the second built-in route (`{"provider":"antigravity"}`, or when the
user asks for Antigravity or Nano Banana); read
[antigravity-generation.md](antigravity-generation.md) for its handoff and delivery.

For an explicitly selected external API, `image-provider.example.json` shows
the endpoint configuration format. A model name does not select a provider.
An external adapter's configured `models` list is the user-approved set.

## Adapters

| Route | When | Availability / budget check |
|---|---|---|
| [imagegen skill](imagegen-generation.md) | Default, or `"provider": "imagegen"` | Runs through the Codex bridge; its session must expose the built-in tool; no external API price quote or Poe preflight |
| [Antigravity](antigravity-generation.md) | `"provider": "antigravity"`, or the user asks for Antigravity / Nano Banana | Built-in `generate_image` through the Antigravity MCP; returns before the file exists, saves elsewhere as JPEG, does not report the model |
| [scripts/image_generate.mjs](../scripts/image_generate.mjs) | Explicitly configured OpenAI-compatible chat endpoint returning images (official API, local server, relay) | Sourced per-call cost estimate × calls must fit the user-authorized `budget_cap` |
| [scripts/poe_image.mjs](../scripts/poe_image.mjs) | `"provider": "poe"` | Adds live point-balance check; see [poe-image-generation.md](poe-image-generation.md) |
| [scripts/generate_openrouter_schematic.py](../scripts/generate_openrouter_schematic.py) | `"provider": "openrouter"` | See [openrouter-image-generation.md](openrouter-image-generation.md) |

External API adapter rules:

- Run `preflight` before spending. An estimate over the cap stops generation and
  goes to the user; unknown pricing is unverified, not cheap.
- Never retry a charged request automatically. On a connection error, check the
  provider's usage records; recover images from the saved response instead of
  regenerating.
- Keys are read from the configured credential source; never print or store
  them in project files.

Shared rules:

- The provider only generates or edits images. Planning, scientific judgment and
  rendered-output inspection stay with the main agent and local checkers.
- Preserve the prompt, references and original image, plus job/response/usage
  records when the route exposes them. An unavailable receipt is not zero usage.
- Follow the selected route's failure handling. An unavailable built-in tool
  does not authorize switching to Poe, OpenRouter or the imagegen CLI/API fallback.
