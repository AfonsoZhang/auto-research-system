# Built-in image generation through Antigravity (Nano Banana)

Use when `provider` is `antigravity`, or the user asks for Antigravity or Nano
Banana. Like `imagegen`, this is a handoff: Claude Code has no image tool, and
Antigravity's agent generates the image with its built-in `generate_image` tool.
No API key, point balance or per-call price applies; the subscription's platform
limits do.

## Call

- Use the `mcp__antigravity__antigravity` MCP tool (load its schema with
  ToolSearch if deferred) with `cwd` = a project or scratch directory and
  `mode: "accept-edits"`. Pass the prompt, each reference image's absolute path
  and role, and the requested output.
- Ask it to use its built-in image generation only and to reply
  `IMAGE_UNAVAILABLE` instead of drawing with code or calling a paid API.

## Known behaviour (checked on one test generation)

1. **The call returns before the image exists.** The agent delegates to an
   `image-generator` subagent and replies immediately. Treat the reply as
   "started", then wait for the file; do not report success from the reply.
2. **The file is not saved where you ask.** It appears under
   `~/.gemini/antigravity-cli/brain/<threadId>/` with a timestamped name, as
   JPEG even when PNG is requested. Find it there by the returned `threadId`,
   copy it into the project and convert the format if a PNG is needed.
3. **The model is not reported.** The transcript names the tool
   (`generate_image`), not the image model. Record "Antigravity generate_image"
   and the thread ID; call it Nano Banana only if the tool reports that model.

## Inspect and deliver

Open the image with the Read tool, check text, content and dimensions, and apply
the same figure QA as the `imagegen` route. Accept the route only when an actual
image file exists. Generated images are for illustration and exploration, never
evidence figures. Keep the prompt, references and thread ID with the delivered file.
