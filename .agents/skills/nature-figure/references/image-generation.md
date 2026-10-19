# Model-generated images: provider-neutral route

Use for generated illustrations, scenes, visual assets and explicitly requested
AI graphical abstracts. Data plots and exact labelled diagrams use their own routes.

## Provider and model come from configuration

No provider, relay or model is built in. Use, in order:

1. An explicit provider/model choice in the current task.
2. The user's local configuration: `IMAGE_PROVIDER_CONFIG`, else
   `$RESEARCH_ROOT/.tools/image-provider.json` (format: `image-provider.example.json`).
3. If nothing is configured, plan the figure and prompts, report that generation
   needs a configured provider, and continue with the other panels.

A model name does not select a provider. The configured `models` list is the
user-approved set; do not add models to it on your own.

## Adapters

| Adapter | When | Budget check |
|---|---|---|
| [scripts/image_generate.mjs](../scripts/image_generate.mjs) | Default; any OpenAI-compatible chat endpoint returning images (official API, local server, relay) | Sourced per-call cost estimate × calls must fit the user-authorized `budget_cap` |
| [scripts/poe_image.mjs](../scripts/poe_image.mjs) | `"provider": "poe"` | Adds live point-balance check; see [poe-image-generation.md](poe-image-generation.md) |
| [scripts/generate_openrouter_schematic.py](../scripts/generate_openrouter_schematic.py) | `"provider": "openrouter"` | See [openrouter-image-generation.md](openrouter-image-generation.md) |

Shared rules for every adapter:

- Run `preflight` before spending. An estimate over the cap stops generation and
  goes to the user; unknown pricing is unverified, not cheap.
- Never retry a charged request automatically. On a connection error, check the
  provider's usage records; recover images from the saved response instead of
  regenerating.
- The provider only generates or edits images. Planning, scientific judgment and
  rendered-output inspection stay with the main agent and local checkers.
- Keep prompt, references, job, raw response, usage and original image together.
- Keys are read from the environment variable named in the configuration; never
  print or store them in project files.
