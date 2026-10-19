# Built-in image generation through imagegen

Use when `provider` is `imagegen`, the user requests the imagegen skill, or no
external provider is selected. This replaces the earlier Poe default.

## Execute through a Codex session that has the tool

Claude Code has no built-in image-generation tool, so this route always runs as
a bounded handoff to Codex. The `imagegen` skill belongs to Codex
(`$HOME/.codex/skills/.system/imagegen/SKILL.md` in this installation);
keep it as the source of truth rather than copying its scripts or API fallback
into nature-figure. The route needs no `OPENAI_API_KEY`, Poe credential, point
balance or external cost quote.

- Use the local Codex bridge `mcp__codex__codex` (load its schema with
  ToolSearch if it is deferred). Pass `cwd` = the project directory and
  `sandbox: "workspace-write"` so Codex can save into the project, plus the
  prompt, each reference's absolute path and role, the requested outputs and an
  absolute destination path. Do not pass the reviewer model/effort pins; this
  is not a review call and is not traced as one.
- Ask Codex to use its built-in `image_gen` tool following the imagegen skill,
  and to report failure instead of substituting the imagegen CLI, an API, or
  code-drawn placeholders. Merely having the MCP server or the skill file is not
  proof the tool exists: accept the route only when actual image files appear at
  the returned paths. Do not start a research team workflow in Codex.
- If the bridge is unavailable or its session does not expose `image_gen`,
  preserve the prepared prompt and references and report the availability
  blocker. Do not silently use the imagegen CLI, a paid external API or a code
  placeholder for a requested bitmap. The CLI/API fallback requires the user's
  explicit choice and its own setup.

## Generate, inspect and deliver

1. Reuse the figure brief and scientific content checks. Keep labels in English
   unless the user requests otherwise. Identify each input as an edit target,
   reference or supporting asset. Inspect local edit targets with the Read tool
   before the handoff and give Codex their absolute paths as image references.
2. Follow imagegen's built-in mode, including transparent backgrounds and
   preservation of the requested invariants. Request the agreed assets or
   variants; do not run an open-ended generation loop.
3. Open the returned images with the Read tool and inspect scientific meaning,
   text, relationships and actual dimensions. Apply targeted revisions under the
   same task scope, through `mcp__codex__codex-reply` on the same thread.
4. For project deliverables, copy the selected image from its actual returned
   location into the project if Codex left it elsewhere, and retain the prompt,
   references and Codex thread ID. Do not leave a manuscript asset only in
   Codex's generated-image directory. For a preview request, report the image
   path. Preserve existing versions unless replacement was requested.
5. Record that Codex's built-in tool was used, with the thread ID. Record model
   identity and usage only when exposed; do not label it `gpt-image-2` solely
   because the CLI uses that model. Return the final artifact paths and apply the existing figure QA.

Platform usage limits still apply. An unavailable quota counter is not a reason
to require Poe preflight or declare this route unlimited. If the tool reports a
limit or failure, report that result and preserve any completed outputs before
deciding whether another attempt is appropriate.
