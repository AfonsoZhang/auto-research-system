# arXiv packaging (Markdown manuscript → LaTeX source)

Converter: a Markdown-to-LaTeX script handling
(headings, abstract, enumerate, captioned pipe tables, figures, one code block,
numeric citations → thebibliography before the appendix). Copy and adapt it
from a previous paper when one exists.

## Build

- Chain: `manuscript_src.md` ([@key]) → `build.py` → `manuscript.md` →
  `md2tex.py` → `arxiv/main.tex` + `arxiv/figures/*.pdf` → compile → tar.
- Without a system LaTeX, tectonic works. It runs XeTeX;
  arXiv compiles with pdflatex, so keep the source ASCII (map unicode in the
  converter) and use standard packages only.
- Wide tables: wrap each tabular in `adjustbox{max width=\linewidth}`; load
  `adjustbox` in the preamble or the build fails with "Environment adjustbox
  undefined". Align a column `r` only if every body cell is numeric, else `l`.
- Check the PDF visually (overfull tables, figure size) before packing.
- Tarball holds `main.tex` and `figures/` only. arXiv adds `00README.json`
  itself after upload; that is normal. Confirm it names `main.tex` and pdflatex.

## Metadata (write `arxiv_metadata.txt`)

- Title, authors, primary category plus suggested cross-lists, comments
  ("N pages, N figures, N tables"), abstract within 1,920 characters.
- Author block, affiliation and email exactly as the author gives them.
- Title: ask before changing. Model it (RITP) on the closest published paper's form
  when the user asks; a colon is optional.

## After submission

- `submit/NNNNNNN` is the submission identifier, not the arXiv ID. The public
  ID (YYMM.NNNNN) appears at announcement. Record the submission ID in the
  project notes; cite the paper elsewhere only after verifying the public
  page (title, authors, date).
