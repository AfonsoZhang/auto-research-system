# Built-in image generation on Codex

When the configured provider is imagegen, read the installed imagegen skill and
use the image tool exposed in this Codex session directly. There is no handoff
to Claude and no reviewer model pin. A skill file alone does not prove the tool
is available. If it is missing, preserve the prompt and references and report the
blocker; do not silently use a paid API, CLI fallback or code-drawn placeholder.

Keep the existing figure brief, scientific content checks, English labels unless
requested otherwise, explicit edit/reference roles and output destinations.
Inspect edit targets before generating. Follow the imagegen skill for reference
paths, transparency and output handling. Inspect actual images for scientific
meaning, labels, dimensions and relationships; revise through the same image
tool within scope. Copy deliverables from returned locations into the project,
preserve existing versions unless replacement was requested, and retain prompt,
references and available generation identifiers. Record only exposed model and
usage information. Apply existing figure QA and report genuine quota failures.
Other explicitly selected providers retain their existing routes.
