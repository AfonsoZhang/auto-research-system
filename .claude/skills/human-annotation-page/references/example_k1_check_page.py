"""Build the local page for the user's check of the reviewed K1 labels (design: data/full/audit/human_check/design.json).

Usage: python3 study/human_check_page.py
Writes data/full/audit/human_check/k1-check.html and thumbs/. No automatic or reviewed label is shown on the page.
"""
import html as htmllib
import json
import re
from pathlib import Path

from PIL import Image

ROOT = Path(__file__).resolve().parent.parent
AUDIT = ROOT / "data" / "full" / "audit"
OUT = AUDIT / "human_check"
design = json.loads((OUT / "design.json").read_text())
STYLE = re.search(r"(?s)<style>(.*?)</style>", (AUDIT / "user_page" / "browser-check.html").read_text()).group(1)


def tidy(text):
    lines = (re.sub(r"[ \t\r\f\v\xa0]+", " ", ln).strip() for ln in text.split("\n"))
    return re.sub(r"\n{3,}", "\n\n", "\n".join(lines)).strip()


def k1_text(d, rec):
    f = d / rec["k1"].get("file", "")
    raw = f.read_bytes() if f.is_file() else b""
    if f.suffix != ".html" and not rec["k1"].get("ctype", "").startswith("text"):
        return "", f"[{rec['k1'].get('ctype') or 'binary'} body, {len(raw):,} bytes]", 0
    page = raw.decode("utf-8", errors="replace")
    title = re.search(r"(?is)<title[^>]*>(.*?)</title>", page)
    page = re.sub(r"(?is)<(script|style|noscript|template)\b.*?</\1>", " ", page)
    page = re.sub(r"(?is)<head\b.*?</head>|<!--.*?-->", " ", page)
    page = re.sub(r"(?i)<(br|/p|/div|/li|/h[1-6]|/tr|/section|/article|/header|/footer|/nav)\b[^>]*>", "\n", page)
    body = tidy(htmllib.unescape(re.sub(r"<[^>]+>", " ", page)))
    t = tidy(htmllib.unescape(re.sub(r"<[^>]+>", " ", title.group(1)))) if title else ""
    return t, body[:3000], len(body)


items = []
(OUT / "thumbs").mkdir(exist_ok=True)
for n, iid in enumerate(design["items"], 1):
    d = ROOT / "data" / "full" / "items" / iid
    rec = json.loads((d / "record.json").read_text())
    title, text, chars = k1_text(d, rec)
    k2 = rec.get("k2") or {}
    k2t = tidy((d / "k2.txt").read_text(encoding="utf-8", errors="replace")) if (d / "k2.txt").is_file() else ""
    shot = (d / "k2.jpg").is_file()
    if shot:
        im = Image.open(d / "k2.jpg").convert("RGB")
        im = im.resize((400, round(im.height * 400 / im.width)))
        im.crop((0, 0, 400, min(im.height, 625))).save(OUT / "thumbs" / f"{n:02d}.jpg", quality=70)
    items.append({
        "n": n, "id": iid, "url": rec["url"],
        "k1_status": rec["k1"].get("status"), "k1_final": rec["k1"].get("final_url"),
        "title": title, "chars": chars, "text": text,
        "k2_status": k2.get("status"), "k2_final": k2.get("final_url"),
        "k2_chars": len(k2t), "k2_text": k2t[:1500], "shot": shot,
    })

page = """<!doctype html>
<html lang="zh"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>K1 Label Check</title>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=IBM+Plex+Sans:wght@400;500;600&family=IBM+Plex+Mono:wght@400;500&display=swap">
<style>""" + STYLE + """
.texts { display: grid; gap: 10px; min-width: 0; }
.k2 pre { max-height: 180px; color: var(--muted); }
.meta { font-family: var(--mono); font-size: 12px; color: var(--muted); word-break: break-all; }
.answers.sub { padding-left: 4px; }
.answers .q { font-size: 13px; color: var(--muted); margin-right: 4px; }
.answers.sub[hidden] { display: none; }
</style>
</head><body>

<header><div class="wrap">
  <h1>K1 label check: 60 static fetches</h1>
  <div class="prog"><div class="bar"><i id="barfill"></i></div><span id="count">0 / 60</span><span id="status">Connecting…</span></div>
</div></header>

<main class="wrap">
  <div id="offline" class="banner" hidden>This browser blocks local storage for this file, so answers live only until you close the tab. Use "Download answers" before closing.</div>
  <section class="intro">
    <p>Each item shows the <b>static fetch (K1)</b>: what a plain HTTP client got, as title and visible text. The <b>rendered fetch (K2)</b> screenshot and text are shown only as a reference for what the page should contain. You do not need to open the link (you may if unsure).</p>
    <p>Question 1: <b>what type is the K1 response?</b></p>
    <div class="legend">
      <code>A</code><span>Main content of the requested page</span>
      <code>B</code><span>Blocked or access denied</span>
      <code>C</code><span>Challenge (JS or bot check, captcha)</span>
      <code>D</code><span>Navigation, skeleton or shell only, without the main content</span>
      <code>E</code><span>Error, not-found, or a different page (homepage, generic page)</span>
      <code>F</code><span>Parked domain or placeholder</span>
      <code>G</code><span>Consent or cookie wall only</span>
      <code>?</code><span>Unsure</span>
    </div>
    <p>Question 2 (only for A): <b>compared with the K2 reference, is K1's main content complete, or clearly incomplete</b> (large parts of the main text missing)? If K2 itself failed, judge K1 on its own.</p>
    <p>Each click is saved in this browser at once. When done, click <b>Download answers</b> and tell Claude; the file goes to your Downloads folder. The note box is optional. Keyboard: on a focused item, press A–G or ?; then 1 = complete, 2 = clearly incomplete.</p>
  </section>
  <div class="filters" role="group" aria-label="Show">
    <button id="f-all" aria-pressed="true">All</button>
    <button id="f-todo" aria-pressed="false">Not answered</button>
    <button id="export" aria-pressed="false">Download answers</button>
  </div>
  <div id="list"></div>
</main>

<script>
const ITEMS = """ + json.dumps(items, ensure_ascii=False).replace("</", "<\\/") + """;
const TYPES = [["A","Main content"],["B","Blocked"],["C","Challenge"],["D","Nav / shell"],["E","Error / other page"],["F","Parked"],["G","Consent wall"],["?","Unsure"]];
const COMPLETE = [["complete","1 Complete"],["incomplete","2 Clearly incomplete"]];
const answers = {};
const KEY = "k1-check-60-answers";
let storeOk = true, filter = "all";

function el(tag, attrs, ...kids) {
  const e = document.createElement(tag);
  for (const [k, v] of Object.entries(attrs || {})) { if (k === "class") e.className = v; else e.setAttribute(k, v); }
  for (const k of kids) e.append(k);
  return e;
}
const done = a => a && a.type && (a.type !== "A" || a.complete);
const pad = n => String(n).padStart(2, "0");

function render() {
  const list = document.getElementById("list");
  list.textContent = "";
  for (const it of ITEMS) {
    const a = answers[it.id] || {};
    if (filter === "todo" && done(a)) continue;
    const card = el("article", { class: "item" + (done(a) ? " done" : ""), id: "item-" + it.n, tabindex: "0", "aria-label": "Item " + it.n });
    card.append(el("div", { class: "head" }, el("span", { class: "num" }, "#" + pad(it.n)),
      el("a", { class: "url", href: it.url, target: "_blank", rel: "noopener noreferrer" }, it.url)));
    card.append(el("div", { class: "meta" }, "K1: status " + it.k1_status + (it.k1_final && it.k1_final !== it.url ? " → " + it.k1_final : "")));
    const fig = it.shot
      ? el("figure", { class: "shot", style: "margin:0" }, el("img", { src: "thumbs/" + pad(it.n) + ".jpg", alt: "K2 screenshot of item " + it.n, loading: "lazy" }), el("figcaption", {}, "K2 rendered screenshot (reference)"))
      : el("figure", { class: "shot", style: "margin:0" }, el("figcaption", {}, "No K2 screenshot"));
    const k1 = el("div", { class: "text" },
      el("div", { class: "lbl" }, "K1 static text · title: " + (it.title || "(none)") + " · " + it.chars.toLocaleString() + " chars" + (it.chars > 3000 ? " (first 3,000 shown)" : "")),
      el("pre", {}, it.text || "[no visible text]"));
    const k2 = el("div", { class: "text k2" },
      el("div", { class: "lbl" }, "K2 rendered text (reference) · status " + it.k2_status + (it.k2_final && it.k2_final !== it.url ? " → " + it.k2_final : "") + " · " + it.k2_chars.toLocaleString() + " chars" + (it.k2_chars > 1500 ? " (first 1,500)" : "")),
      el("pre", {}, it.k2_text || "[no text]"));
    card.append(el("div", { class: "body" }, fig, el("div", { class: "texts" }, k1, k2)));

    const row = el("div", { class: "answers" }, el("span", { class: "q" }, "Type"));
    for (const [k, label] of TYPES) {
      const b = el("button", { type: "button", "aria-pressed": String(a.type === k), id: "b-" + it.n + "-" + (k === "?" ? "q" : k) }, el("b", {}, k), label);
      b.addEventListener("click", () => save(it, { type: k }));
      row.append(b);
    }
    const sub = el("div", { class: "answers sub" }, el("span", { class: "q" }, "Main content vs K2"));
    if (a.type !== "A") sub.hidden = true;
    for (const [k, label] of COMPLETE) {
      const b = el("button", { type: "button", "aria-pressed": String(a.complete === k), id: "c-" + it.n + "-" + k }, label);
      b.addEventListener("click", () => save(it, { complete: k }));
      sub.append(b);
    }
    const note = el("input", { class: "note", id: "note-" + it.n, type: "text", placeholder: "Note (optional)", "aria-label": "Note for item " + it.n });
    note.value = a.note || "";
    note.addEventListener("change", () => save(it, { note: note.value }));
    const tail = el("div", { class: "answers" }, note, el("span", { class: "saved", id: "s-" + it.n }, done(a) ? "Saved" : (a.type === "A" ? "Answer question 2" : "")));
    card.append(row, sub, tail);
    card.addEventListener("keydown", (e) => {
      if (e.target.tagName === "INPUT") return;
      const k = e.key.toUpperCase();
      if (["A","B","C","D","E","F","G","?"].includes(k)) { e.preventDefault(); save(it, { type: k }); }
      else if ((k === "1" || k === "2") && (answers[it.id] || {}).type === "A") { e.preventDefault(); save(it, { complete: k === "1" ? "complete" : "incomplete" }); }
    });
    list.append(card);
  }
  const n = ITEMS.filter(it => done(answers[it.id])).length;
  document.getElementById("count").textContent = n + " / " + ITEMS.length;
  document.getElementById("barfill").style.width = (100 * n / ITEMS.length) + "%";
}

function save(it, patch) {
  const next = Object.assign({ n: it.n, url: it.url, type: null, complete: null, note: "" }, answers[it.id] || {}, patch, { at: new Date().toISOString() });
  if (next.type !== "A") next.complete = null;
  answers[it.id] = next;
  const focusId = document.activeElement && document.activeElement.id;
  render();
  if (focusId && document.getElementById(focusId)) document.getElementById(focusId).focus();
  persist();
  const s = document.getElementById("s-" + it.n);
  if (s && !storeOk) { s.textContent = "Kept until tab closes"; s.className = "saved err"; }
}

function persist() {
  try { localStorage.setItem(KEY, JSON.stringify(answers)); storeOk = true; }
  catch (e) { storeOk = false; document.getElementById("offline").hidden = false; }
  document.getElementById("status").textContent = storeOk ? "Autosave on" : "Not saving";
}

document.getElementById("export").addEventListener("click", () => {
  const out = ITEMS.map(it => Object.assign({ item_id: it.id }, answers[it.id] || { n: it.n, url: it.url, type: null, complete: null, note: "" }));
  const blob = new Blob([JSON.stringify(out, null, 1)], { type: "application/json" });
  const a = document.createElement("a");
  a.href = URL.createObjectURL(blob); a.download = "k1_check_answers.json";
  document.body.append(a); a.click(); a.remove();
});

document.getElementById("f-all").addEventListener("click", () => { filter = "all"; setFilter(); });
document.getElementById("f-todo").addEventListener("click", () => { filter = "todo"; setFilter(); });
function setFilter() {
  document.getElementById("f-all").setAttribute("aria-pressed", String(filter === "all"));
  document.getElementById("f-todo").setAttribute("aria-pressed", String(filter === "todo"));
  render();
}

try { Object.assign(answers, JSON.parse(localStorage.getItem(KEY) || "{}")); } catch (e) { storeOk = false; }
render();
persist();
</script>
</body></html>
"""
(OUT / "k1-check.html").write_text(page)
print(OUT / "k1-check.html", len(items), "items")
