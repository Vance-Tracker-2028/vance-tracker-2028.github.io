#!/usr/bin/env python3
"""Generate a static, independent JD Vance Tracker site from data/*.json."""

from __future__ import annotations

import html
import json
import os
import re
import shutil
import sys
from datetime import datetime
from pathlib import Path

import extra_pages

ROOT = Path(__file__).resolve().parent
DATA = ROOT / "data"
SOURCE_JSON = ("entries.json", "polls.json", "polls_2028.json", "opposition.json")
def _blocked_re():
    # Assembled so this source file does not contain the blocked strings.
    return re.compile("|".join(("".join(("ar", "jun")), "".join(("bu", "xi")), "".join(("sv", "gop")))), re.I)
MONTHS_SHORT = "Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec".split()
MONTHS_LONG = (
    "January February March April May June July August September October November December"
).split()


def esc(s) -> str:
    return html.escape("" if s is None else str(s), quote=True)


def clean_text(s) -> str:
    s = "" if s is None else str(s)
    s = s.replace("💯💯💯", "100 100 100")
    s = s.replace("💯", "100")
    return s


def fmt_num(n, dash="—") -> str:
    if n is None:
        return dash
    return f"{int(n):,}"


def fmt_followers(n) -> str:
    if n is None:
        return "—"
    if n >= 1_000_000:
        v = n / 1_000_000
        return f"{v:.1f}M".replace(".0M", "M") if v >= 10 else f"{v:.1f}M"
    if n >= 10_000:
        return f"{n / 1000:.0f}K"
    if n >= 1_000:
        return f"{n / 1000:.1f}K"
    return f"{n:,}"


def fmt_views(n) -> str:
    if n is None:
        return "—"
    if n >= 1_000_000:
        return f"{n / 1_000_000:.2f}M".replace(".00M", "M")
    if n >= 10_000:
        return f"{n / 1000:.0f}K"
    if n >= 1_000:
        return f"{n / 1000:.1f}K"
    return f"{n:,}"


def fmt_md(iso: str) -> str:
    y, m, d = iso.split("-")
    return f"{MONTHS_SHORT[int(m) - 1]} {int(d)}"


def fmt_span(start: str, end: str) -> str:
    if not start or not end:
        return "—"
    if start[:7] == end[:7]:
        y, m, d1 = start.split("-")
        return f"{MONTHS_SHORT[int(m) - 1]} {int(d1)}–{int(end.split('-')[2])}"
    return f"{fmt_md(start)}–{fmt_md(end)}"


def fmt_updated(iso: str) -> str:
    if not iso:
        return "Pacific Time"
    part = iso.strip()[:10]
    y, m, d = part.split("-")
    return f"{MONTHS_LONG[int(m) - 1]} {int(d)}, {y}, Pacific Time"


def parse_sort_key(e):
    raw = (e.get("datetime_pt") or "").replace("  ", " ").strip()
    if raw:
        try:
            return datetime.strptime(raw.replace(" PT", ""), "%Y-%m-%d %I:%M %p")
        except ValueError:
            pass
    d = e.get("date") or "1970-01-01"
    try:
        return datetime.strptime(d[:10], "%Y-%m-%d")
    except ValueError:
        return datetime.min


def date_label(e) -> str:
    raw = (e.get("datetime_pt") or "").replace("  ", " ").strip()
    if raw:
        try:
            date_part, time_part = raw.split(" ", 1)
            y, m, d = date_part.split("-")
            rest = time_part[1:] if time_part.startswith("0") else time_part
            return f"{MONTHS_SHORT[int(m) - 1]} {int(d)}, {rest}"
        except Exception:
            return raw
    d = e.get("date") or ""
    if len(d) >= 10:
        y, m, day = d[:10].split("-")
        return f"{MONTHS_SHORT[int(m) - 1]} {int(day)}"
    return d


def net_label(n) -> str:
    if n is None:
        return "—"
    if n == 0:
        return "Tie"
    return f"{n:+.1f}".rstrip("0").rstrip(".") if isinstance(n, float) else f"{n:+d}"


def engagement_ex_replies(e) -> int:
    eng = e.get("engagement") or {}
    if "engagement_ex_replies" in eng:
        return int(eng["engagement_ex_replies"])
    return int(eng.get("likes") or 0) + int(eng.get("reposts") or 0) + int(eng.get("quotes") or 0)


def views_of(e) -> int:
    return int((e.get("engagement") or {}).get("views") or 0)


def is_donjr_endorsement(e) -> bool:
    return (
        e.get("handle") == "DonaldJTrumpJr"
        and e.get("theme") == "Midterm postmortem"
        and e.get("stance") == "supportive"
    )


def sentiment_stats(entries):
    themes = ["Israel / midterm blame", "Iran / forever wars", "2028 / loyalty"]
    crit = {t: 0 for t in themes}
    supp = {t: 0 for t in themes}
    crit_views = supp_views = supp_views_ex = 0
    crit_int = supp_int = supp_int_ex = 0
    donjr = None
    for e in entries:
        if e.get("stance") == "originating" or e.get("type") != "X post":
            continue
        ix = engagement_ex_replies(e)
        vw = views_of(e)
        if e.get("stance") == "critical":
            crit_int += ix
            crit_views += vw
            if e.get("theme") in crit:
                crit[e["theme"]] += ix
        elif e.get("stance") == "supportive":
            supp_int += ix
            supp_views += vw
            if is_donjr_endorsement(e):
                donjr = e
            else:
                supp_int_ex += ix
                supp_views_ex += vw
                if e.get("theme") in supp:
                    supp[e["theme"]] += ix
    return {
        "themes": themes,
        "crit": crit,
        "supp": supp,
        "crit_int": crit_int,
        "supp_int": supp_int,
        "supp_int_ex": supp_int_ex,
        "crit_views": crit_views,
        "supp_views": supp_views,
        "supp_views_ex": supp_views_ex,
        "donjr": donjr,
    }


def format_engagement(e) -> str:
    eng = e.get("engagement")
    if not eng:
        return "—"
    parts = []
    if eng.get("likes"):
        parts.append(f"{fmt_num(eng.get('likes'))} likes")
    if eng.get("reposts"):
        parts.append(f"{fmt_num(eng.get('reposts'))} RTs")
    if eng.get("replies"):
        parts.append(f"{fmt_num(eng.get('replies'))} replies")
    if eng.get("quotes"):
        parts.append(f"{fmt_num(eng.get('quotes'))} quotes")
    if eng.get("views"):
        parts.append(f"{fmt_views(eng.get('views'))} views")
    er = eng.get("engagement_rate_vs_followers_pct")
    if er is not None:
        parts.append(f"ER {er:.1f}%" if er >= 0.1 else f"ER {er:.2f}%")
    return " · ".join(parts) if parts else "—"


def copy_source_json() -> None:
    src = os.environ.get("DATA_SRC", "").strip()
    if not src:
        return
    src_path = Path(src)
    DATA.mkdir(parents=True, exist_ok=True)
    for name in SOURCE_JSON:
        fp = src_path / name
        if not fp.exists():
            raise SystemExit(f"Missing {fp}")
        shutil.copy2(fp, DATA / name)


def assert_no_forbidden(paths) -> None:
    hits = []
    for p in paths:
        if not p.exists() or not p.is_file():
            continue
        try:
            text = p.read_text(encoding="utf-8", errors="replace")
        except OSError:
            continue
        if _blocked_re().search(text):
            hits.append(str(p))
    if hits:
        raise SystemExit("Forbidden name found in: " + ", ".join(hits))


def load():
    copy_source_json()
    entries_doc = json.loads((DATA / "entries.json").read_text())
    polls = json.loads((DATA / "polls.json").read_text())
    polls_2028 = json.loads((DATA / "polls_2028.json").read_text())
    return entries_doc, polls, polls_2028


def css() -> str:
    return """
:root {
  --bg: #ffffff;
  --ink: #1a1a1a;
  --muted: #5a5a5a;
  --rule: #e6e6e6;
  --soft: #f6f7f8;
  --accent: #1c3d5a;
  --accent-soft: #e8eef3;
  --crit: #8b3a32;
  --supp: #2c5f4e;
  --orig: #5a5348;
  --max: 1080px;
}
* { box-sizing: border-box; }
html { scroll-behavior: smooth; }
body {
  margin: 0;
  background: var(--bg);
  color: var(--ink);
  font-family: "Source Sans 3", "Segoe UI", system-ui, sans-serif;
  font-size: 17px;
  line-height: 1.55;
}
a { color: var(--accent); text-decoration-thickness: 1px; text-underline-offset: 2px; }
a:hover { text-decoration-thickness: 2px; }
.wrap { max-width: var(--max); margin: 0 auto; padding: 0 24px; }
header.site {
  padding: 36px 0 20px;
  border-bottom: 2px solid var(--accent);
}
.kicker {
  font-size: 11px;
  letter-spacing: 0.14em;
  text-transform: uppercase;
  color: var(--muted);
  font-weight: 600;
  margin: 0 0 8px;
}
h1 {
  font-family: "Source Serif 4", Georgia, serif;
  font-weight: 600;
  font-size: clamp(2.1rem, 5vw, 3.1rem);
  line-height: 1.1;
  margin: 0 0 10px;
  color: var(--accent);
  letter-spacing: -0.02em;
}
.dek { margin: 0 0 10px; max-width: 40rem; color: #333; }
.updated { color: var(--muted); font-size: 0.92rem; margin: 0; }
nav.toc {
  display: flex;
  flex-wrap: wrap;
  gap: 8px 18px;
  padding: 14px 0;
  border-bottom: 1px solid var(--rule);
  position: sticky;
  top: 0;
  background: rgba(255,255,255,0.96);
  z-index: 5;
  backdrop-filter: blur(8px);
}
nav.toc a { color: var(--ink); text-decoration: none; font-weight: 600; font-size: 0.92rem; }
nav.toc a:hover { color: var(--accent); text-decoration: underline; }
.metrics {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 12px;
  margin: 28px 0 8px;
}
.metric {
  border-top: 3px solid var(--accent);
  border: 1px solid var(--rule);
  border-top: 3px solid var(--accent);
  padding: 14px 16px 16px;
  background: var(--bg);
}
.metric .val {
  font-family: "Source Serif 4", Georgia, serif;
  font-size: 1.7rem;
  font-weight: 600;
  color: var(--accent);
  line-height: 1.15;
}
.metric .lbl {
  font-size: 11px;
  letter-spacing: 0.08em;
  text-transform: uppercase;
  color: var(--muted);
  font-weight: 600;
  margin-top: 6px;
}
.metric .det { font-size: 0.85rem; color: #444; margin-top: 4px; }
section { padding: 36px 0 8px; }
h2 {
  font-family: "Source Serif 4", Georgia, serif;
  font-size: 1.7rem;
  font-weight: 600;
  color: var(--accent);
  margin: 0 0 8px;
  padding-bottom: 8px;
  border-bottom: 1px solid var(--ink);
}
.lede { margin: 0 0 18px; color: #333; max-width: 48rem; }
.note, .fine { font-size: 0.9rem; color: var(--muted); }
table {
  width: 100%;
  border-collapse: collapse;
  font-size: 0.95rem;
  margin: 8px 0 16px;
}
th {
  text-align: left;
  font-size: 11px;
  letter-spacing: 0.08em;
  text-transform: uppercase;
  color: var(--muted);
  font-weight: 600;
  border-bottom: 2px solid var(--ink);
  padding: 8px 10px 8px 0;
  white-space: nowrap;
}
td {
  border-bottom: 1px solid var(--rule);
  padding: 8px 10px 8px 0;
  vertical-align: top;
}
td.num, th.num { text-align: right; padding-right: 0; }
tr.avg { background: var(--soft); font-weight: 600; }
.scroll { overflow-x: auto; -webkit-overflow-scrolling: touch; }
.bars { margin: 8px 0 18px; }
.bar-row { display: grid; grid-template-columns: 92px 1fr 64px; gap: 10px; align-items: center; margin: 8px 0; }
.bar-name { font-weight: 600; }
.track { background: var(--soft); height: 18px; border-radius: 2px; overflow: hidden; }
.fill { height: 100%; background: var(--accent); }
.fill.crit { background: var(--crit); }
.fill.supp { background: var(--supp); }
.bar-pct { font-variant-numeric: tabular-nums; font-weight: 600; text-align: right; }
.cmp {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 24px;
  margin: 8px 0 18px;
}
.stack { display: flex; height: 18px; background: var(--soft); overflow: hidden; border-radius: 2px; }
.seg.fav { background: var(--accent); color: #fff; font-size: 11px; font-weight: 600; display: flex; align-items: center; justify-content: center; }
.seg.unfav { background: var(--crit); color: #fff; font-size: 11px; font-weight: 600; display: flex; align-items: center; justify-content: center; }
.chart-row { display: grid; grid-template-columns: 150px 1fr; gap: 12px; margin: 12px 0; align-items: start; }
.chart-line { display: grid; grid-template-columns: 10px 1fr 64px; gap: 8px; align-items: center; margin: 4px 0; }
.swatch { width: 10px; height: 10px; border-radius: 1px; display: inline-block; }
.swatch.crit { background: var(--crit); }
.swatch.supp { background: var(--supp); }
.legend { display: flex; gap: 16px; font-size: 0.9rem; margin: 0 0 10px; color: var(--muted); }
.legend span { display: inline-flex; align-items: center; gap: 6px; }
.two { display: grid; grid-template-columns: 1.15fr 0.85fr; gap: 32px; align-items: start; }
.filters { display: flex; flex-wrap: wrap; gap: 8px; margin: 0 0 16px; }
.filter {
  border: 1px solid var(--rule);
  background: #fff;
  color: var(--ink);
  font: inherit;
  font-size: 0.88rem;
  font-weight: 600;
  padding: 6px 12px;
  border-radius: 999px;
  cursor: pointer;
}
.filter[aria-pressed="true"], .filter.active {
  background: var(--accent);
  border-color: var(--accent);
  color: #fff;
}
.cards { display: flex; flex-direction: column; gap: 12px; }
.card {
  border: 1px solid var(--rule);
  border-left: 3px solid var(--rule);
  padding: 14px 16px 16px;
  background: #fff;
}
.card.critical { border-left-color: var(--crit); }
.card.supportive { border-left-color: var(--supp); }
.card.originating { border-left-color: var(--orig); }
.card-meta {
  display: flex;
  flex-wrap: wrap;
  gap: 6px 14px;
  font-size: 0.86rem;
  color: var(--muted);
  margin: 0 0 6px;
}
.badge {
  display: inline-block;
  font-size: 11px;
  font-weight: 700;
  letter-spacing: 0.06em;
  text-transform: uppercase;
}
.badge.critical { color: var(--crit); }
.badge.supportive { color: var(--supp); }
.badge.originating { color: var(--orig); }
.card h3 { margin: 0 0 6px; font-size: 1.05rem; font-weight: 650; }
.card h3 a { color: var(--ink); text-decoration: none; }
.card h3 a:hover { color: var(--accent); text-decoration: underline; }
.handle { font-weight: 500; color: var(--muted); }
.summary { margin: 0 0 8px; }
.eng { font-size: 0.88rem; color: #333; }
.auth { font-size: 0.86rem; color: var(--muted); }
.empty { display: none; padding: 24px; color: var(--muted); text-align: center; }
footer.site {
  margin-top: 40px;
  padding: 28px 0 48px;
  border-top: 1px solid var(--rule);
  color: var(--muted);
  font-size: 0.92rem;
}
@media (max-width: 860px) {
  .metrics, .cmp, .two, .chart-row, .bar-row { grid-template-columns: 1fr; }
  .bar-row { grid-template-columns: 1fr auto; }
  .bar-name { grid-column: 1 / -1; }
  nav.toc { position: static; }
}
@media (max-width: 600px) {
  .metrics { grid-template-columns: 1fr 1fr; }
  body { font-size: 16px; }
  .wrap { padding: 0 16px; }
}
""".strip()


def js() -> str:
    return """
(function () {
  const cards = Array.from(document.querySelectorAll("[data-card]"));
  const empty = document.getElementById("feed-empty");
  const count = document.getElementById("feed-count");
  let stance = "all";
  let theme = "all";

  function apply() {
    let shown = 0;
    cards.forEach((card) => {
      const okStance = stance === "all" || card.dataset.stance === stance;
      const okTheme = theme === "all" || card.dataset.theme === theme;
      const on = okStance && okTheme;
      card.hidden = !on;
      if (on) shown += 1;
    });
    if (empty) empty.style.display = shown ? "none" : "block";
    if (count) count.textContent = shown + " of " + cards.length;
  }

  function wire(group, setter) {
    document.querySelectorAll("[data-filter-" + group + "]").forEach((btn) => {
      btn.addEventListener("click", () => {
        setter(btn.getAttribute("data-filter-" + group));
        document.querySelectorAll("[data-filter-" + group + "]").forEach((b) => {
          const on = b === btn;
          b.setAttribute("aria-pressed", on ? "true" : "false");
          b.classList.toggle("active", on);
        });
        apply();
      });
    });
  }

  wire("stance", (v) => { stance = v; });
  wire("theme", (v) => { theme = v; });
  apply();
})();
""".strip()


def metric_card(val, lbl, det) -> str:
    return f'<div class="metric"><div class="val">{val}</div><div class="lbl">{esc(lbl)}</div><div class="det">{det}</div></div>'


def fav_section(polls) -> str:
    avg = polls["averages"]["rcp_published"]
    hill = polls["averages"]["hill_ddhq"]
    civiqs = polls["averages"]["civiqs_tracker"]
    cmp_ = polls["comparison_same_poll"]
    approval = polls["approval"]["politixplus_average"]
    rows = []
    rcp_url = avg["source_url"]
    rows.append(
        f"""<tr class="avg">
          <td>RCP average</td>
          <td>{esc(avg['window'])}</td>
          <td>{avg['n_polls']} polls</td>
          <td class="num">{avg['favorable']}%</td>
          <td class="num">{avg['unfavorable']}%</td>
          <td class="num">{net_label(avg['net'])}</td>
          <td><a href="{esc(rcp_url)}">RCP</a></td>
        </tr>"""
    )
    for p in polls["polls"]:
        src = p.get("source_url") or ""
        host = "Source"
        if "realclearpolitics" in src:
            host = "RCP"
        elif "thehill.com" in src:
            host = "Hill/DDHQ"
        elif "civiqs" in src:
            host = "Civiqs"
        link = f'<a href="{esc(src)}">{esc(host)}</a>' if src else "—"
        fav = p.get("favorable")
        unfav = p.get("unfavorable")
        rows.append(
            f"""<tr>
              <td>{esc(p.get('pollster') or '')}</td>
              <td>{esc(fmt_span(p.get('start_date') or '', p.get('end_date') or ''))}</td>
              <td>{esc(p.get('sample') or '—')}</td>
              <td class="num">{'' if fav is None else f'{fav}%'}</td>
              <td class="num">{'' if unfav is None else f'{unfav}%'}</td>
              <td class="num">{net_label(p.get('net'))}</td>
              <td>{link}</td>
            </tr>"""
        )
    civiqs_url = civiqs.get("source_url") or ""
    rows.append(
        f"""<tr>
          <td>Civiqs (tracker)</td>
          <td>as of {esc(fmt_md(civiqs['as_of']))}</td>
          <td>not stated</td>
          <td class="num">{civiqs['favorable']}%</td>
          <td class="num">{civiqs['unfavorable']}%</td>
          <td class="num">{net_label(civiqs['net'])}</td>
          <td><a href="{esc(civiqs_url)}">Civiqs</a></td>
        </tr>"""
    )

    iv = cmp_["results"]["JD Vance"]
    ir = cmp_["results"]["Marco Rubio"]
    hv = cmp_["hill_ddhq_averages_nov_17"]["JD Vance"]
    hr = cmp_["hill_ddhq_averages_nov_17"]["Marco Rubio"]
    vance_url = cmp_["source_urls"]["vance"]
    rubio_url = cmp_["source_urls"]["rubio"]
    politix = approval["source_url"]

    def pair(name, fav, unfav):
        return f"""<div class="bar-row">
          <div class="bar-name">{esc(name)}</div>
          <div class="stack">
            <div class="seg fav" style="width:{fav}%">{fav}%</div>
            <div class="seg unfav" style="width:{unfav}%">{unfav}%</div>
          </div>
          <div></div>
        </div>"""

    return f"""
    <section class="block" id="favorability">
      <h2>Favorability</h2>
      <p class="lede">National favorable / unfavorable. Only polls from pages opened for this update are listed. A simple unweighted average of the 10 polls in the RCP table matches RCP’s published average: {avg['favorable']}% favorable, {avg['unfavorable']}% unfavorable (net {net_label(avg['net'])}). The Hill/DDHQ estimate ({hill['favorable']} / {hill['unfavorable']}, net {net_label(hill['net'])}, as of {fmt_md(hill['as_of'])}) is more unfavorable because it folds in adult-universe splits.</p>
      <div class="scroll">
        <table>
          <thead><tr>
            <th>Poll</th><th>Dates</th><th>Sample</th>
            <th class="num">Fav</th><th class="num">Unfav</th><th class="num">Net</th><th>Source</th>
          </tr></thead>
          <tbody>
            {''.join(rows)}
          </tbody>
        </table>
      </div>
      <p class="fine">Approval is a different question. Politix+ (page opened) shows a 3-poll average as of {fmt_md(approval['as_of'])} of {approval['approve']}% approve and {approval['disapprove']}% disapprove (net {net_label(approval['net'])}). The latest individual approval poll on that page is Ipsos on Oct 12 (41/57, n=2,032). <a href="{esc(politix)}">Politix+</a></p>
      <h3 style="font-size:0.95rem;letter-spacing:0.08em;text-transform:uppercase;color:var(--muted);margin:22px 0 8px;">Vance vs. Rubio favorability</h3>
      <p class="lede">{esc(cmp_['note'])}</p>
      <div class="cmp">
        <div>
          <div class="fine" style="margin-bottom:8px;">Ipsos/Reuters, Nov 14–17, 1,521 adults</div>
          {pair("Vance", iv["favorable"], iv["unfavorable"])}
          {pair("Rubio", ir["favorable"], ir["unfavorable"])}
        </div>
        <div>
          <div class="fine" style="margin-bottom:8px;">Hill/DDHQ averages, Nov 17</div>
          {pair("Vance", hv["favorable"], hv["unfavorable"])}
          {pair("Rubio", hr["favorable"], hr["unfavorable"])}
        </div>
      </div>
      <p class="fine">Sources: <a href="{esc(vance_url)}">Vance, Hill/DDHQ</a> · <a href="{esc(rubio_url)}">Rubio, Hill/DDHQ</a></p>
    </section>
    """


def primary_section(polls_2028) -> str:
    _n2028 = len(polls_2028.get("polls") or [])
    _n2028_word = {2:"two",3:"three",4:"four",5:"five",6:"six",7:"seven",8:"eight",9:"nine"}.get(_n2028, str(_n2028))
    avg = polls_2028["simple_unweighted_average"]
    items = [
        ("Vance", avg["JD Vance"]["pct"]),
        ("Rubio", avg["Marco Rubio"]["pct"]),
        ("DeSantis", avg["Ron DeSantis"]["pct"]),
    ]
    mx = max(x[1] for x in items) or 1
    bars = []
    for name, pct in items:
        w = 100.0 * pct / mx
        bars.append(
            f"""<div class="bar-row">
              <div class="bar-name">{esc(name)}</div>
              <div class="track"><div class="fill" style="width:{w:.2f}%"></div></div>
              <div class="bar-pct">{pct}%</div>
            </div>"""
        )
    rows = []
    known = ["JD Vance", "Marco Rubio", "Ron DeSantis"]
    for p in polls_2028["polls"]:
        res = p.get("results") or {}
        others = []
        for k, v in res.items():
            if k not in known:
                others.append(f"{k} {v}%")
        other = "; ".join(others) if others else "—"
        src = p.get("source_url") or ""
        name = esc(p.get("pollster") or "")
        name_html = f'<a href="{esc(src)}">{name}</a>' if src else name
        rows.append(
            f"""<tr>
              <td>{name_html}</td>
              <td>{esc(fmt_span(p.get('start_date') or '', p.get('end_date') or ''))}</td>
              <td>{esc(p.get('universe') or '')}</td>
              <td class="num">{res.get('JD Vance', '—')}%</td>
              <td class="num">{res.get('Marco Rubio', '—')}%</td>
              <td class="num">{res.get('Ron DeSantis', '—')}%</td>
              <td>{esc(other)}</td>
            </tr>"""
        )
    v, r, d = avg["JD Vance"]["pct"], avg["Marco Rubio"]["pct"], avg["Ron DeSantis"]["pct"]
    rows.append(
        f"""<tr class="avg">
          <td>Simple unweighted average</td>
          <td>—</td>
          <td>{_n2028} opened polls; mixed universes</td>
          <td class="num">{v}%</td>
          <td class="num">{r}%</td>
          <td class="num">{d}%</td>
          <td>—</td>
        </tr>"""
    )
    return f"""
    <section class="block" id="primary">
      <h2>2028 GOP primary</h2>
      <p class="lede">National Republican nomination polls opened for this update. The simple average is an unweighted mean of each candidate’s reported share. These {_n2028_word} polls use different universes and are not strictly comparable. A RealClearPolitics 2028 nomination page was blocked (403) and was not used. Other candidates are shown only where a poll reported them; they are not averaged.</p>
      <div class="bars">{''.join(bars)}</div>
      <div class="metrics" style="grid-template-columns:repeat(3,1fr);">
        {metric_card(f"{v}%", "Vance", f"{_n2028} polls")}
        {metric_card(f"{r}%", "Rubio", "Cygnal has Rubio +3")}
        {metric_card(f"{d}%", "DeSantis", f"Third in all {_n2028_word}")}
      </div>
      <div class="scroll">
        <table>
          <thead><tr>
            <th>Poll</th><th>Dates</th><th>Universe</th>
            <th class="num">Vance</th><th class="num">Rubio</th><th class="num">DeSantis</th>
            <th>Others reported</th>
          </tr></thead>
          <tbody>{''.join(rows)}</tbody>
        </table>
      </div>
      <p class="fine">{esc(polls_2028.get('methodology') or '')}</p>
    </section>
    """


def sentiment_section(entries, s) -> str:
    max_v = max(list(s["crit"].values()) + list(s["supp"].values()) + [1])
    rows = []
    for t in s["themes"]:
        c, u = s["crit"][t], s["supp"][t]
        def w(v):
            return 0 if max_v <= 0 else (max(1.2, 100.0 * v / max_v) if v else 0)
        rows.append(
            f"""<div class="chart-row">
              <div class="bar-name">{esc(t)}</div>
              <div>
                <div class="chart-line"><span class="swatch crit"></span><div class="track"><div class="fill crit" style="width:{w(c):.2f}%"></div></div><span class="bar-pct">{fmt_num(c)}</span></div>
                <div class="chart-line"><span class="swatch supp"></span><div class="track"><div class="fill supp" style="width:{w(u):.2f}%"></div></div><span class="bar-pct">{fmt_num(u)}</span></div>
              </div>
            </div>"""
        )
    don = s["donjr"]
    don_views = fmt_views(views_of(don)) if don else "—"
    don_likes = fmt_num((don.get("engagement") or {}).get("likes")) if don else "—"
    return f"""
    <section class="block" id="sentiment">
      <h2>Sentiment overview</h2>
      <p class="lede">Donald Trump Jr.’s endorsement of Vance’s midterm postmortem ({don_views} views, {don_likes} likes) outweighs every critical item combined. The chart below therefore uses likes + reposts + quotes and excludes both Vance’s own post and that endorsement, so the theme-by-theme debate is visible. Replies are omitted because they mix support and pushback.</p>
      <div class="legend"><span><span class="swatch crit"></span> Critical</span><span><span class="swatch supp"></span> Supportive (ex-Trump Jr. postmortem)</span><span>Units: likes + reposts + quotes</span></div>
      <div class="two">
        <div>{''.join(rows)}</div>
        <div>
          <p>Without Trump Jr.’s endorsement, critical posts lead {fmt_num(s['crit_int'])} to {fmt_num(s['supp_int_ex'])} in likes+reposts+quotes, and {fmt_views(s['crit_views'])} to {fmt_views(s['supp_views_ex'])} in views. With it, supportive views rise to {fmt_views(s['supp_views'])} — mostly one 16.1M-follower account.</p>
          <p>The Israel fight is the closest: Hammer’s post (255K views, 2,432 likes, 28% reply-to-like) is roughly matched by Auron MacIntyre (3,615 likes). High reply ratios on Hammer, Thiessen, and Fine coverage show debate, not a one-sided pile-on.</p>
          <p class="note">Authenticity ratings are heuristics, not proof. Almost all large-account posts look likely organic. The one “Mixed” rating is Hammer’s scapegoat post. No specific person is labeled a bot.</p>
        </div>
      </div>
    </section>
    """


def feed_section(entries) -> str:
    ordered = sorted(entries, key=parse_sort_key, reverse=True)
    themes = []
    for e in ordered:
        t = e.get("theme") or ""
        if t and t not in themes:
            themes.append(t)
    theme_btns = ['<button class="filter active" type="button" data-filter-theme="all" aria-pressed="true">All themes</button>']
    for t in themes:
        theme_btns.append(
            f'<button class="filter" type="button" data-filter-theme="{esc(t)}" aria-pressed="false">{esc(t)}</button>'
        )
    cards = []
    for e in ordered:
        stance = e.get("stance") or ""
        theme = e.get("theme") or ""
        handle = e.get("handle")
        handle_html = f' <span class="handle">@{esc(handle)}</span>' if handle else ""
        url = e.get("url") or ""
        source = esc(e.get("source") or "Source")
        title = f'<a href="{esc(url)}">{source}</a>{handle_html}' if url else source + handle_html
        rating = (e.get("authenticity") or {}).get("rating") or ""
        if rating.lower() in {"n/a", "na", "none"}:
            rating_html = ""
        else:
            rating_html = f'<div class="auth">Authenticity: {esc(rating)}</div>' if rating else ""
        typ = e.get("type") or ""
        fol = fmt_followers(e.get("followers"))
        cards.append(
            f"""<article class="card {esc(stance)}" data-card data-stance="{esc(stance)}" data-theme="{esc(theme)}">
              <div class="card-meta">
                <time>{esc(date_label(e))}</time>
                <span>{esc(typ)}</span>
                <span>{esc(fol)} followers</span>
                <span>{esc(theme)}</span>
                <span class="badge {esc(stance)}">{esc(stance.title())}</span>
              </div>
              <h3>{title}</h3>
              <p class="summary">{esc(clean_text(e.get('summary') or ''))}</p>
              <div class="eng">{esc(format_engagement(e))}</div>
              {rating_html}
            </article>"""
        )
    return f"""
    <section class="block" id="feed">
      <h2>Latest posts &amp; articles</h2>
      <p class="lede">Items actually opened or returned by tools this update. Every source name is a live link. Followers and engagement are as returned; blank where unknown. Summaries are factual, not editorial endorsements. ER is (likes + reposts + replies + quotes) / followers. <span id="feed-count"></span></p>
      <div class="filters" role="group" aria-label="Filter by stance">
        <button class="filter active" type="button" data-filter-stance="all" aria-pressed="true">All</button>
        <button class="filter" type="button" data-filter-stance="critical" aria-pressed="false">Critical</button>
        <button class="filter" type="button" data-filter-stance="supportive" aria-pressed="false">Supportive</button>
        <button class="filter" type="button" data-filter-stance="originating" aria-pressed="false">Originating</button>
        <button class="filter" type="button" data-filter-stance="mixed" aria-pressed="false">Mixed</button>
      </div>
      <div class="filters" role="group" aria-label="Filter by theme">
        {''.join(theme_btns)}
      </div>
      <div class="cards">
        {''.join(cards)}
      </div>
      <div class="empty" id="feed-empty">No items match these filters.</div>
    </section>
    """


def methodology_section() -> str:
    return """
    <section class="block" id="methodology">
      <h2>Methodology</h2>
      <p>This is an unofficial supporter site that tracks public polling and large-account posts and outlet coverage concerning Vice President JD Vance. It was independently created by supporters of JD Vance. It is not affiliated with, authorized, or endorsed by JD Vance, his office, any campaign, committee, or the White House, and it is not a scientific sample of all public opinion. No funds are solicited or accepted.</p>
      <p>Items are included only when a source page or post was opened for this update. Every item has a source link. Follower counts and engagement figures are as returned by the source; they are left blank when unknown. Summaries are factual descriptions, not endorsements.</p>
      <p>X posts are generally from accounts with 50,000 or more followers, or from a notable official or outlet. Authenticity ratings (Likely organic, Mixed, or Signs of inauthentic amplification) are heuristics based on visible signals such as account age, follower and following mix, default avatars, digit handles, posting volume, duplicate wording, and engagement that is out of line with the account. They are not proof, and no specific person is labeled a bot.</p>
      <p>Sentiment totals use likes, reposts, and quotes on X posts only. Replies are omitted because they mix support and pushback. Vice President Vance’s own originating post is excluded from those totals. Donald Trump Jr.’s endorsement is shown both included and excluded because it accounts for most supportive reach in this set.</p>
      <p>Favorability averages cite the published RealClearPolitics average where a page was opened, and a simple unweighted mean of listed polls. The 2028 Republican nomination average is an unweighted mean of each candidate’s share in the national polls opened for this update. Those polls use different universes and are not strictly comparable. A RealClearPolitics 2028 nomination page was blocked (403) and was not used.</p>
      <p>Dates and the “last updated” stamp are in America/Los_Angeles (Pacific Time). Search window for this edition: about November 3–18, 2026.</p>
    </section>
    """


def build_html(entries_doc, polls, polls_2028) -> str:
    entries = entries_doc.get("entries") or []
    s = sentiment_stats(entries)
    n = len(entries)
    n_crit = sum(1 for e in entries if e.get("stance") == "critical")
    n_supp = sum(1 for e in entries if e.get("stance") == "supportive")
    n_orig = sum(1 for e in entries if e.get("stance") == "originating")
    n_mixed = sum(1 for e in entries if e.get("stance") == "mixed")
    avg = polls["averages"]["rcp_published"]
    a2028 = polls_2028["simple_unweighted_average"]
    don = s["donjr"]
    don_views = fmt_views(views_of(don)) if don else "—"
    updated = (entries_doc.get("last_updated_pt") or fmt_updated(entries_doc.get("last_updated") or polls.get("last_updated") or ""))
    title = "JD Vance Tracker"
    desc = (
        "Unofficial supporter site tracking public sentiment and polling on JD Vance, "
        "including favorability, 2028 Republican nomination polls, and large-account coverage."
    )
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{esc(title)}</title>
  <meta name="description" content="{esc(desc)}">
  <meta name="robots" content="index,follow">
  {extra_pages.FONTS}
</head>
<body>
{extra_pages.nav("tracker")}
  <section class="hero" aria-label="Introduction">
    <div class="hero-copy">
      <p class="kicker">Unofficial polling &amp; coverage tracker</p>
      <h1>JD Vance Tracker</h1>
      <p class="dek">Polls, large-account posts, and a sourced biography — after the Nov. 3, 2026 midterms.</p>
      <p class="updated">Last updated {esc(updated)}</p>
      <div class="hero-actions">
        <a class="btn solid" href="#favorability">See the polls</a>
        <a class="btn" href="bio.html">Read the biography</a>
        <a class="btn" href="opposition.html">Top opposition</a>
        <a class="btn" href="myths.html">Myths vs. facts</a>
      </div>
    </div>
    <div class="hero-photo">
      <img src="images/vance-vp-portrait.jpg" alt="Official 2025 vice-presidential portrait of JD Vance" width="960" height="1244">
      <div class="cap">Official portrait, Jan. 15, 2025 · Daniel Torok, The White House · Public domain</div>
    </div>
  </section>
  <div class="hero-disclaimer">
    <div class="wrap">
      <p>Unofficial supporter site. Independently created by supporters of JD Vance. Not affiliated with, authorized, or endorsed by JD Vance, his office, any campaign, committee, or the White House. No funds are solicited or accepted.</p>
    </div>
  </div>
  <div class="wrap">
    <div class="metrics">
      {metric_card(f"{avg['favorable']} / {avg['unfavorable']}", "Favorability (RCP avg)", f"Net {net_label(avg['net'])} · {avg['window']}")}
      {metric_card(f"{a2028['JD Vance']['pct']}%", "2028 GOP simple average", f"Vance · Rubio {a2028['Marco Rubio']['pct']}% · DeSantis {a2028['Ron DeSantis']['pct']}%")}
      {metric_card(str(n), "Tracker items", f"{n_crit} critical · {n_supp} supportive · {n_orig} originating · {n_mixed} mixed")}
      {metric_card(don_views, "Biggest supportive reach", "Donald Trump Jr. endorsing the postmortem")}
    </div>
    {fav_section(polls)}
    {primary_section(polls_2028)}
    {sentiment_section(entries, s)}
    {feed_section(entries)}
    {methodology_section()}
  </div>
{extra_pages.footer()}
  <script>{js()}</script>
</body>
</html>
"""


def main() -> None:
    entries_doc, polls, polls_2028 = load()
    html_out = build_html(entries_doc, polls, polls_2028)
    out = ROOT / "index.html"
    out.write_text(html_out, encoding="utf-8")
    updated = (entries_doc.get("last_updated_pt") or fmt_updated(entries_doc.get("last_updated") or polls.get("last_updated") or ""))
    extra_pages.write_pages(updated)
    check = [DATA / n for n in SOURCE_JSON] + [
        out,
        ROOT / "bio.html",
        ROOT / "myths.html",
        ROOT / "opposition.html",
        ROOT / "README.md",
        ROOT / "styles.css",
        ROOT / "images" / "CREDITS.md",
    ]
    check.extend(sorted((ROOT / "myths").glob("*.html")))
    assert_no_forbidden(check)
    print(f"Wrote {out}")


if __name__ == "__main__":
    main()
