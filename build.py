#!/usr/bin/env python3
"""Generate index.html: the Winter Siege deployment plan.

Reads data/squads.csv (rank, player, squad, rank_badge, power, current) and
assigns every squad to a stronghold ("front-wardens" layout, see
docs/strategy.md; 112 squads):

  * ranks 1-2    -> Wardens of Strongholds 2 and 3
  * ranks 3-5    -> Wardens of Strongholds 4, 5 and 6: a front can't be
                    cleared without killing a 5-Heart whale
  * ranks 6-23   -> Strongholds 2, 3 (9 each, snake): the wall in front of 1
  * ranks 24-72  -> Strongholds 4, 5, 6 (snake): mid squads make every front
                    cost real attacks; the empty slots land here
  * ranks 73-92  -> Strongholds 2, 3 (10 more each)
  * ranks 93-112 -> Stronghold 1 (reached last; 3 stars each, kept safe)
  * Warden       -> strongest squad in each stronghold

Once the plan is applied in-game, the CSV's `assigned` column pins each squad
where it is; squads without one (late sign-ups) are placed into free slots,
fronts first, without moving anyone else.

`python3 build.py <layout>` builds another layout from LAYOUTS into
<layout>.html (ignoring pins). Edit OVERRIDES to pin a squad somewhere;
sim.py compares layouts.
"""
import csv
import html
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).parent
CSV = ROOT / "data" / "squads.csv"
OUT = ROOT / "index.html"

STRONGHOLDS = {
    1: dict(tier="Empowered", stars=3, cap=20),
    2: dict(tier="Advanced", stars=2, cap=20),
    3: dict(tier="Advanced", stars=2, cap=20),
    4: dict(tier="Primitive", stars=1, cap=20),
    5: dict(tier="Primitive", stars=1, cap=20),
    6: dict(tier="Primitive", stars=1, cap=20),
}
# (stronghold snake order, per-stronghold cap) for each pool, strongest first.
# A cap of None means "whatever is left after the fixed pools", so the empty
# slots always land in that pool.
LAYOUTS = {
    # front-wardens: biggest two anchor 2/3, next three are front Wardens,
    # then graded. Best in sim.py against every enemy tested.
    "front-wardens": [
        ([2, 3], 1),
        ([4, 5, 6], 1),
        ([2, 3], 9),
        ([4, 5, 6], None),
        ([2, 3], 10),
        ([1], 20),
    ],
    # graded: wall of whales in 2/3, mid squads at the fronts, weakest in 1
    "graded": [
        ([2, 3], 10),
        ([4, 5, 6], None),
        ([2, 3], 10),
        ([1], 20),
    ],
    # balanced: one whale Warden per stronghold (Gemini's idea), then graded
    "balanced": [
        ([1, 2, 3, 4, 5, 6], 1),
        ([2, 3], 9),
        ([4, 5, 6], None),
        ([2, 3], 10),
        ([1], 19),
    ],
}
LAYOUT = "front-wardens"
POOLS = LAYOUTS[LAYOUT]

# (player, squad) -> stronghold.  Applied after the draft; the displaced
# squad is NOT re-balanced, so keep overrides few.
OVERRIDES = {}


def load():
    rows = list(csv.DictReader(open(CSV, encoding="utf-8")))
    for r in rows:
        r["power"] = int(r["power"])
        r["rank"] = int(r["rank"])
        r["current"] = int(r.get("current") or 1)
        r["assigned"] = int(r["assigned"]) if r.get("assigned") else None
    rows.sort(key=lambda r: -r["power"])
    return rows


LATE_ORDER = [4, 5, 6, 2, 3, 1]   # where late sign-ups go, by free slots


def assign_pinned(rows):
    """Keep every pinned squad where it is; put the rest into free slots."""
    plan = {(r["player"], r["squad"]): r["assigned"] for r in rows if r["assigned"]}
    count = defaultdict(int)
    for sh in plan.values():
        count[sh] += 1
    for r in rows:  # strongest first
        if r["assigned"]:
            continue
        free = [sh for sh in LATE_ORDER if count[sh] < STRONGHOLDS[sh]["cap"]]
        assert free, "no free slots"
        fronts = [sh for sh in free if sh in (4, 5, 6)]
        sh = min(fronts, key=lambda s: count[s]) if fronts else free[0]
        count[sh] += 1
        plan[(r["player"], r["squad"])] = sh
    return plan


def snake(order):
    """Yield stronghold ids forever in snake order: a,b,c,c,b,a,a,b,c,..."""
    seq = order + order[::-1]
    while True:
        yield from seq


def assign(rows, use_pins=True):
    if use_pins and any(r.get("assigned") for r in rows):
        plan = assign_pinned(rows)
        by_sh = defaultdict(list)
        for r in rows:
            r["target"] = plan[(r["player"], r["squad"])]
            by_sh[r["target"]].append(r)
        for lst in by_sh.values():
            lst.sort(key=lambda r: -r["power"])
            for i, r in enumerate(lst):
                r["warden"] = i == 0
        return by_sh
    plan = {}
    remaining = list(rows)
    fixed = sum(cap * len(order) for order, cap in POOLS if cap is not None)
    for order, cap in POOLS:
        n = cap * len(order) if cap is not None else len(rows) - fixed
        gen = snake(order)
        count = defaultdict(int)
        take, remaining = remaining[:n], remaining[n:]
        per = cap if cap is not None else -(-n // len(order))
        for r in take:
            sh = next(gen)
            while count[sh] >= per:
                sh = next(gen)
            count[sh] += 1
            plan[(r["player"], r["squad"])] = sh
    assert not remaining, f"{len(remaining)} squads unassigned"
    for sh, info in STRONGHOLDS.items():
        assert sum(1 for v in plan.values() if v == sh) <= info["cap"], f"SH{sh} over capacity"
    plan.update(OVERRIDES)
    by_sh = defaultdict(list)
    for r in rows:
        r["target"] = plan[(r["player"], r["squad"])]
        by_sh[r["target"]].append(r)
    for sh, lst in by_sh.items():
        lst.sort(key=lambda r: -r["power"])
        for i, r in enumerate(lst):
            r["warden"] = i == 0
    return by_sh


def fmt(n):
    return f"{n/1e9:.2f}B" if n >= 1e9 else f"{n/1e6:.0f}M"


def stars_for(r, sh):
    s = STRONGHOLDS[sh]["stars"]
    return s * 2 if r["warden"] else s


def card(sh, squads):
    info = STRONGHOLDS[sh]
    total = sum(stars_for(r, sh) for r in squads)
    power = sum(r["power"] for r in squads)
    rows_html = []
    for r in squads:
        cls = "warden" if r["warden"] else ""
        move = "" if r["current"] == sh else f'<span class="move">from {r["current"]}</span>'
        rows_html.append(
            f'<tr class="{cls}"><td class="rk">{r["rank"]}</td>'
            f'<td class="nm">{html.escape(r["player"])} <span class="sq">S{r["squad"]}</span>'
            f'{" <span class=\"badge\">Warden</span>" if r["warden"] else ""}</td>'
            f'<td class="pw">{fmt(r["power"])}</td>'
            f'<td class="st">{"★" * stars_for(r, sh)}</td><td class="mv">{move}</td></tr>'
        )
    return f"""
<section class="sh tier-{info['tier'].lower()}" id="sh{sh}">
  <header>
    <h2>Stronghold {sh} <small>{info['tier']}</small></h2>
    <div class="meta">{len(squads)}/{info['cap']} squads · {total} ★ · {fmt(power)} · {info['stars']}★ per squad, Warden {info['stars']*2}★</div>
  </header>
  <table>{''.join(rows_html)}</table>
</section>"""


def player_table(rows):
    by_player = defaultdict(list)
    for r in rows:
        by_player[r["player"]].append(r)
    out = []
    for name in sorted(by_player, key=str.casefold):
        cells = []
        for r in sorted(by_player[name], key=lambda r: r["squad"]):
            moved = "" if r["current"] == r["target"] else " moved"
            w = " ★W" if r["warden"] else ""
            cells.append(f'<td class="dest{moved}">S{r["squad"]} → <b>SH{r["target"]}</b>{w}<small>{fmt(r["power"])}</small></td>')
        out.append(f'<tr><td class="nm">{html.escape(name)}</td>{"".join(cells)}</tr>')
    return "".join(out)


def main():
    global POOLS, OUT
    import sys
    if len(sys.argv) > 1:
        POOLS = LAYOUTS[sys.argv[1]]
        if sys.argv[1] != LAYOUT:
            OUT = ROOT / f"{sys.argv[1]}.html"
    rows = load()
    by_sh = assign(rows, use_pins=len(sys.argv) == 1)
    total_stars = sum(stars_for(r, sh) for sh, lst in by_sh.items() for r in lst)
    moves = sum(r["current"] != r["target"] for r in rows)
    cards = {sh: card(sh, by_sh[sh]) for sh in STRONGHOLDS}
    page = TEMPLATE.format(
        n_squads=len(rows),
        n_players=len({r["player"] for r in rows}),
        total_stars=total_stars,
        moves=moves,
        sh1=cards[1], sh2=cards[2], sh3=cards[3], sh4=cards[4], sh5=cards[5], sh6=cards[6],
        players=player_table(rows),
    )
    OUT.write_text(page, encoding="utf-8")
    print(f"wrote {OUT}: {len(rows)} squads, {total_stars} stars, {moves} moves")


TEMPLATE = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Winter Siege Deployment</title>
<style>
:root {{ --bg:#eef3f8; --card:#fff; --ink:#1b2a3a; --mute:#5b6b7b; --line:#d6dfe8;
  --emp:#2b5fb8; --adv:#3d8a6e; --pri:#8a7a3d; --warden:#fff4d6; --move:#c0392b; }}
@media (prefers-color-scheme: dark) {{ :root {{ --bg:#121a24; --card:#1b2634; --ink:#e6edf5; --mute:#9fb0c2; --line:#2c3a4b; --warden:#3a3320; }} }}
* {{ box-sizing:border-box }}
body {{ margin:0; padding:20px 16px 48px; background:var(--bg); color:var(--ink); font:14px/1.45 system-ui,-apple-system,Segoe UI,Roboto,sans-serif }}
h1 {{ margin:0 0 4px; font-size:26px }}
.sub {{ color:var(--mute); margin-bottom:20px }}
.map {{ display:grid; gap:16px; grid-template-columns:repeat(3,1fr); max-width:1280px; margin:0 auto }}
.map .row2 {{ grid-column:1/-1; display:grid; gap:16px; grid-template-columns:1fr 1fr; padding:0 16.6% }}
.map .row3 {{ grid-column:1/-1; padding:0 33.3% }}
@media (max-width:900px) {{ .map, .map .row2 {{ grid-template-columns:1fr; padding:0 }} .map .row3 {{ padding:0 }} }}
.sh {{ background:var(--card); border:1px solid var(--line); border-top:5px solid var(--pri); border-radius:10px; padding:12px 14px; overflow-x:auto }}
.tier-empowered {{ border-top-color:var(--emp) }} .tier-advanced {{ border-top-color:var(--adv) }}
.sh h2 {{ margin:0; font-size:18px }} .sh h2 small {{ font-weight:normal; color:var(--mute); font-size:13px; margin-left:6px }}
.meta {{ color:var(--mute); font-size:12px; margin:2px 0 8px }}
table {{ width:100%; border-collapse:collapse }}
td {{ padding:4px 6px; border-top:1px solid var(--line); white-space:nowrap }}
td.rk {{ color:var(--mute); width:2.2em; text-align:right }} td.nm {{ width:100% ; white-space:normal }}
.sq {{ color:var(--mute); font-size:12px }} td.pw {{ text-align:right; font-variant-numeric:tabular-nums }}
td.st {{ color:#d4a017; letter-spacing:-1px }} td.mv {{ font-size:11px }}
tr.warden {{ background:var(--warden); font-weight:600 }}
.badge {{ font-size:10px; text-transform:uppercase; background:#d4a017; color:#1b1b1b; border-radius:4px; padding:1px 5px; margin-left:4px; vertical-align:middle }}
.move {{ color:var(--move) }}
.arrows {{ text-align:center; color:var(--mute); font-size:12px; grid-column:1/-1 }}
.wrap {{ max-width:1280px; margin:0 auto }}
.players {{ background:var(--card); border:1px solid var(--line); border-radius:10px; padding:12px 14px; margin-top:28px; overflow-x:auto }}
.players td.dest {{ white-space:nowrap }} .players td.dest small {{ color:var(--mute); margin-left:6px }}
.players td.moved b {{ color:var(--move) }}
.rules {{ margin-top:28px; display:grid; gap:16px; grid-template-columns:repeat(auto-fit,minmax(280px,1fr)) }}
.rules div {{ background:var(--card); border:1px solid var(--line); border-radius:10px; padding:12px 14px }}
.rules h3 {{ margin:0 0 6px; font-size:15px }} .rules ul {{ margin:0; padding-left:18px }} .rules li {{ margin:3px 0 }}
</style>
</head>
<body>
<div class="wrap">
<h1>Winter Siege — Deployment Plan</h1>
<div class="sub">{n_squads} squads from {n_players} players · {total_stars} ★ on the board · {moves} squads need to move · highlighted row = Warden · red text = current stronghold</div>

<div class="map">
  {sh4}{sh5}{sh6}
  <div class="arrows">Paths: 4 → 2 · 5 → 2 and 3 · 6 → 3 · 2 and 3 → 1. A stronghold is attackable only after every squad in the stronghold before it on the path is defeated.</div>
  <div class="row2">{sh2}{sh3}</div>
  <div class="row3">{sh1}</div>
</div>

<div class="rules">
  <div><h3>Why this layout</h3><ul>
    <li>Stars are lost only when a squad loses all its Hearts. A weak squad dies in 4–5 attacks; a 1B+ squad forces morale-baiting first (floor 60%) and costs 15–30. The enemy will take the cheapest path: a front → the Advanced stronghold behind it → Stronghold 1.</li>
    <li>Each front's Warden is a whale (5 Hearts, 2★). A front can't be cleared — and the Advanced ring can't be opened — without killing one, so an enemy that can't bait a whale down never gets past the fronts. Mid-strength squads (ranks 24–72) fill the fronts so all three cost about the same.</li>
    <li>The two biggest squads and the next 18 form the wall in Strongholds 2 and 3: once a front does fall, the reachable targets are worth 2★ and expensive.</li>
    <li>Stronghold 1 is reached last, so it holds the weakest squads: 60★ that are only in danger after a front and an Advanced stronghold have both been cleared. Simulated against an equal enemy this layout loses ~50–110★ where "strongest in the core" loses ~85–155★; against a weaker enemy ~40–50★. Against an enemy 15%+ stronger, no layout holds (130–190★ lost) — placement decides close matchups.</li>
    <li>The 8 empty slots sit in the fronts, where a squad is worth 1★; Strongholds 1–3 are full. Placement doesn't affect attacking: every squad attacks at full strength wherever it is garrisoned.</li>
  </ul></div>
  <div><h3>R4/R5 checklist</h3><ul>
    <li>Manage Squads → batch adjust during Preparation (Wed–Thu UTC). Lock is Thu 24:00 UTC.</li>
    <li>Appoint the Warden in each stronghold <b>after</b> moving squads; moving a Warden's squad drops the role.</li>
    <li>Anyone who leaves the alliance during Preparation must re-register both squads.</li>
    <li>Members: gear on the registered heroes before lock. City bonus, state position, President skill, territory buffs and exclusive-gear skills don't count.</li>
  </ul></div>
  <div><h3>Battle day</h3><ul>
    <li>Win = first to zero the enemy; else most Stars left; tie → surviving troop power.</li>
    <li>Attacks accrue over the day (3 per squad at start, +1 every 2h). Against an equal enemy the race is tight: both sides can wipe the other in ~24h if attacks aren't wasted, so speed and not wasting attacks matter.</li>
    <li>Front tier first, cheapest kills first. Agree the order before anyone attacks.</li>
    <li>Bottom-tier squads bait morale on their strong defenders (−10% per defender win above 80%, then −5%, floor 60%); mid squads take the weakened target; whales finish. A lost Heart resets morale to 100%, so repeat per Heart.</li>
    <li>Everyone attacks, including squads outside the top 20 and squads already eliminated.</li>
  </ul></div>
</div>

<div class="players">
  <h2 style="margin:0 0 8px;font-size:18px">Player lookup</h2>
  <table>{players}</table>
</div>
</div>
</body>
</html>
"""

if __name__ == "__main__":
    main()
