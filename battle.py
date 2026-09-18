#!/usr/bin/env python3
"""Matchup analysis and attack plan for Winter Siege.

    python3 battle.py <friendly.csv> <enemy.csv> <FRIENDLY> <ENEMY> <out-prefix>

Both CSVs are garrison files: stronghold,rank,player,squad,power,warden (the
format of data/enemy.csv; build.py writes ours to data/garrison.csv). Produces
<out-prefix>.html and docs/<out-prefix>.md: both layouts, who is stronger where,
which squads can't be killed at the 60% morale floor, a simulation in both
directions, and a phased attack plan with roles for the friendly side.

Kill model (see sim.py): an attack is a safe win when attacker power >= SAFE x
the defender's effective power (power x morale). Bait = a deliberately lost
attack that drops the defender's morale (-10% above 80%, -5% at or below,
floor 60%); losing a Heart resets it to 100%.
"""
import csv
import html
import random
import sys
from collections import defaultdict
from pathlib import Path

import build
import sim

ROOT = Path(__file__).parent
SAFE = 1.07
FLOOR = 0.6
STARS = {1: 3, 2: 2, 3: 2, 4: 1, 5: 1, 6: 1}
NEXT = {4: [2], 5: [2, 3], 6: [3], 2: [1], 3: [1], 1: []}


def fmt(n):
    return f"{n/1e9:.2f}B" if n >= 1e9 else f"{n/1e6:.0f}M"


def load(path):
    by = defaultdict(list)
    for r in csv.DictReader(open(path, encoding="utf-8")):
        r["power"] = int(r["power"]); r["sh"] = int(r["stronghold"]); r["rank"] = int(r["rank"])
        r["warden"] = r["warden"] == "1"; r["hearts"] = 5 if r["warden"] else 4
        r["stars"] = STARS[r["sh"]] * (2 if r["warden"] else 1)
        by[r["sh"]].append(r)
    for l in by.values():
        l.sort(key=lambda r: -r["power"])
    for sh in range(1, 7):
        by.setdefault(sh, [])          # a stronghold with no screenshots stays empty
    return by


def morale_drop(m):
    return max(FLOOR, round(m - (.10 if m > .80 else .05), 2))


def classify(r, attackers):
    """(class, #attackers that beat it outright, expected attacks to remove it)."""
    if attackers[0] < r["power"] * FLOOR * SAFE:
        return "unkillable", 0, None
    outright = sum(p >= r["power"] * SAFE for p in attackers)
    cls = "easy" if outright >= 12 else "mid" if outright >= 3 else "hard"
    m, baits = 1.0, 0
    while sum(p >= r["power"] * m * SAFE for p in attackers) < 3 and m > FLOOR:
        m = morale_drop(m); baits += 1
    return cls, outright, r["hearts"] * (baits + 1)


def annotate(defenders, attackers):
    for l in defenders.values():
        for r in l:
            r["cls"], r["outright"], r["cost"] = classify(r, attackers)


def sh_cost(by, sh):
    return sum(r["cost"] or 0 for r in by[sh]), any(r["cls"] == "unkillable" for r in by[sh])


def missing(by):
    return [sh for sh in range(1, 7) if not by[sh]]


def simulate(defenders, attackers, budgets=(3, 4, 5, 6, 8)):
    out = []
    for a in budgets:
        random.seed(1); p = sim.run(defenders, attackers, a, "path", runs=8)
        random.seed(1); g = sim.run(defenders, attackers, a, "greedy", runs=8)
        out.append((a, p, g))
    return out


def phases(enemy, fname):
    """Attack order for the friendly side against `enemy` (already annotated)."""
    ph = []
    fronts = {sh: sh_cost(enemy, sh) for sh in (4, 5, 6)}
    killable_fronts = [sh for sh, (c, unk) in fronts.items() if not unk]
    if not killable_fronts:
        return [("No way in", "Every front stronghold has a squad we cannot kill even at the 60% morale floor. We can only farm the killable squads at the fronts (1★ each).", [r for sh in (4, 5, 6) for r in enemy[sh] if r["cls"] != "unkillable"])], []
    cheapest = min(killable_fronts, key=lambda s: fronts[s][0])
    first = 5 if 5 in killable_fronts and fronts[5][0] <= fronts[cheapest][0] * 1.15 else cheapest
    opened = NEXT[first]
    w = enemy[first][0]
    ph.append((f"Phase 1 — open the map: clear Stronghold {first}",
               f"{'Opens both 2 and 3' if first == 5 else f'Opens Stronghold {opened[0]}'}; {'the cheapest front' if first == cheapest else 'not the very cheapest front, but worth it for the double unlock'} at ~{fronts[first][0]} attacks for {sum(r['stars'] for r in enemy[first])}★. "
               f"Warden {w['player']} S{w['squad']} ({fmt(w['power'])}, 5 Hearts) needs attackers over {fmt(w['power']*SAFE)}"
               + (" — no baiting needed." if w["cls"] in ("easy", "mid") else f" after baiting (~{w['cost']} attacks)."),
               list(enemy[first])))
    cheap = [r for sh in opened for r in enemy[sh] if r["cls"] == "easy"]
    if cheap:
        ph.append((f"Phase 2 — farm the cheap 2★ squads in Stronghold{'s' if len(opened) > 1 else ''} {' and '.join(map(str, opened))}",
                   f"{len(cheap)} squads worth 2★ each that 12+ of our squads beat outright: ~{sum(r['cost'] for r in cheap)} attacks for {2*len(cheap)}★. Best Stars-per-attack on their board. Leave their whales alone for now.",
                   cheap))
    rest = [sh for sh in (4, 5, 6) if sh != first and not fronts[sh][1]]
    if rest:
        ph.append((f"Phase 3 — clear Stronghold{'s' if len(rest) > 1 else ''} {' and '.join(map(str, rest))}",
                   " + ".join(str(fronts[s][0]) for s in rest) + f" attacks for {sum(r['stars'] for s in rest for r in enemy[s])}★. Wardens: "
                   + ", ".join(f"{enemy[s][0]['player']} S{enemy[s][0]['squad']} ({fmt(enemy[s][0]['power'])}, needs ≥ {fmt(enemy[s][0]['power']*SAFE)})" for s in rest) + ".",
                   [r for s in rest for r in enemy[s]]))
    adv_open = sorted(set(opened) | {s for r_ in rest for s in NEXT[r_]})
    cheap2 = [r for sh in adv_open for r in enemy[sh] if r["cls"] == "easy" and r not in cheap]
    if cheap2:
        ph.append((f"Phase 3b — cheap 2★ squads newly reachable in Stronghold {', '.join(str(s) for s in adv_open if any(r['sh']==s for r in cheap2))}",
                   f"{len(cheap2)} squads, ~{sum(r['cost'] for r in cheap2)} attacks for {2*len(cheap2)}★.", cheap2))
    mid = [r for sh in adv_open for r in enemy[sh] if r["cls"] == "mid"]
    if mid:
        ph.append((f"Phase 4 — mid 2★ targets in Stronghold{'s' if len(adv_open) > 1 else ''} {' and '.join(map(str, adv_open))}",
                   f"{len(mid)} squads that 3–11 of our squads beat outright, or that need a bait or two: ~{sum(r['cost'] for r in mid)} attacks for {2*len(mid)}★.", mid))
    hard = [r for sh in adv_open for r in enemy[sh] if r["cls"] == "hard"]
    if hard:
        ph.append(("Phase 5 — only with leftover attempts: the hard 2★ targets",
                   f"{len(hard)} squads that need several baits per Heart before a top squad can finish: ~{sum(r['cost'] for r in hard)} attacks for {sum(r['stars'] for r in hard)}★. Poor value.", hard))
    # Stronghold 1: reachable only if an Advanced stronghold can be fully cleared
    clearable_adv = [s for s in adv_open if not sh_cost(enemy, s)[1]]
    if clearable_adv:
        s = min(clearable_adv, key=lambda s: sh_cost(enemy, s)[0])
        easy1 = [r for r in enemy[1] if r["cls"] in ("easy", "mid")]
        ph.append((f"Phase 6 — if Stronghold {s} is fully cleared (~{sh_cost(enemy, s)[0]} attacks): farm Stronghold 1",
                   f"{len(easy1)} squads worth 3★ that we beat outright or nearly: ~{sum(r['cost'] for r in easy1)} attacks for {sum(r['stars'] for r in easy1)}★. "
                   + ("Their Stronghold 1 can be zeroed." if not sh_cost(enemy, 1)[1] else "Their Stronghold 1 Warden is unkillable, so it can never be zeroed."),
                   easy1))
    else:
        ph.append(("Stronghold 1 — out of reach",
                   "Every Advanced stronghold we can open contains a squad we cannot kill, so their Stronghold 1 can never be unlocked. Don't plan around it.", []))
    unk = [r for l in enemy.values() for r in l if r["cls"] == "unkillable"]
    return ph, unk


def roles(friendly):
    out = []
    for r in sorted((r for l in friendly.values() for r in l), key=lambda r: -r["power"]):
        p = r["power"]
        role = ("Finisher — save attempts for baited whales; don't spend them on fronts" if p >= 1.0e9 else
                "Heavy hitter — front Wardens and the 600–750M squads" if p >= 7.0e8 else
                "Line hitter — fronts and the cheap 2★ farm" if p >= 4.5e8 else
                "Cleanup / bait — squads under your threshold; bait duty on whales when called")
        out.append((r, p / SAFE, role))
    return out


def main():
    fpath, epath, F, E, prefix = sys.argv[1:6]
    friendly, enemy = load(fpath), load(epath)
    fpow = sorted((r["power"] for l in friendly.values() for r in l), reverse=True)
    epow = sorted((r["power"] for l in enemy.values() for r in l), reverse=True)
    annotate(enemy, fpow); annotate(friendly, epow)
    ph, unk_e = phases(enemy, F)
    unk_f = [r for l in friendly.values() for r in l if r["cls"] == "unkillable"]
    e_stars = sum(r["stars"] for l in enemy.values() for r in l)
    f_stars = sum(r["stars"] for l in friendly.values() for r in l)
    ceiling = e_stars - sum(r["stars"] for r in unk_e)
    we_attack = simulate(enemy, fpow)      # stars they lose
    they_attack = simulate(friendly, epow)  # stars we lose
    rl = roles(friendly)

    def layout_desc(by):
        core, adv, fr = sum(r["power"] for r in by[1]), sum(r["power"] for s in (2, 3) for r in by[s]), sum(r["power"] for s in (4, 5, 6) for r in by[s])
        tot = core + adv + fr
        if core / tot > 0.28: kind = "core-heavy (whales in Stronghold 1)"
        elif fr / tot > 0.42: kind = "front-heavy (strength at the fronts)"
        else: kind = "middle-heavy (strength in Strongholds 2 and 3)"
        return kind, core, adv, fr
    fk, fc, fa, ff = layout_desc(friendly); ek, ec, ea, ef = layout_desc(enemy)

    # verdict from the equal-budget simulation at 4 and 5 attacks
    ours4 = next(p for a, p, g in we_attack if a == 4); theirs4 = next(p for a, p, g in they_attack if a == 4)
    ours5 = next(p for a, p, g in we_attack if a == 5); theirs5 = next(p for a, p, g in they_attack if a == 5)
    margin = ((e_stars - ours4) - (f_stars - theirs4), (e_stars - ours5) - (f_stars - theirs5))  # + means enemy keeps more
    if margin[0] < -15 and margin[1] < -15: verdict = f"{F} is favoured: at equal activity we keep more Stars than they do."
    elif margin[0] > 15 and margin[1] > 15: verdict = f"{E} is favoured: at equal activity they keep more Stars. {F} wins only by out-attacking them."
    else: verdict = "Too close to call at equal activity — whoever uses more of their attacks wins."

    # ---------------- markdown ----------------
    md = [f"# {F} vs [{E}] — matchup analysis and attack plan", "",
          f"Generated {__import__('datetime').date.today()} from scouted garrisons (`{Path(fpath).name}`, `{Path(epath).name}`).", "",
          *( [f"> **Not scouted:** {F} Stronghold{'s' if len(missing(friendly))>1 else ''} {', '.join(map(str, missing(friendly)))} — no screenshots in the folder; its squads are left out of {F}'s totals and of the defence simulation.", ""] if missing(friendly) else [] ),
          *( [f"> **Not scouted:** [{E}] Stronghold{'s' if len(missing(enemy))>1 else ''} {', '.join(map(str, missing(enemy)))}.", ""] if missing(enemy) else [] ),
          "## Who is stronger", "",
          f"| | {F} | [{E}] |", "|---|---|---|",
          f"| Garrison power | {fmt(sum(fpow))} | {fmt(sum(epow))} |",
          f"| Squads ≥ 1B / ≥ 2B | {sum(p>=1e9 for p in fpow)} / {sum(p>=2e9 for p in fpow)} | {sum(p>=1e9 for p in epow)} / {sum(p>=2e9 for p in epow)} |",
          f"| Strongest squad | {fmt(fpow[0])} | {fmt(epow[0])} |",
          f"| Stars on board | {f_stars} | {e_stars} |",
          f"| Layout | {fk}: core {fmt(fc)}, middle {fmt(fa)}, fronts {fmt(ff)} | {ek}: core {fmt(ec)}, middle {fmt(ea)}, fronts {fmt(ef)} |",
          f"| Squads the other side cannot kill (60% floor) | {len(unk_f)}: " + (", ".join(f"{r['player']} S{r['squad']} {fmt(r['power'])} (SH{r['sh']})" for r in unk_f) or "none") + f" | {len(unk_e)}: " + (", ".join(f"{r['player']} S{r['squad']} {fmt(r['power'])} (SH{r['sh']})" for r in unk_e) or "none") + " |",
          "", "### Per stronghold", "", f"| Stronghold | {F} power · ★ · Warden | [{E}] power · ★ · Warden | attacks for us to clear | attacks for them to clear |", "|---|---|---|---|---|"]
    def side_cell(by, sh):
        if not by[sh]:
            return "not scouted"
        w = by[sh][0]
        return f"{fmt(sum(r['power'] for r in by[sh]))} · {sum(r['stars'] for r in by[sh])}★ · {w['player']} S{w['squad']} {fmt(w['power'])}"
    def clear_cell(by, sh):
        if not by[sh]:
            return "?"
        c, u = sh_cost(by, sh)
        return "never (unkillable squad)" if u else f"~{c}"
    for sh in (1, 2, 3, 4, 5, 6):
        md.append(f"| {sh} ({build.STRONGHOLDS[sh]['tier']}) | {side_cell(friendly, sh)} | {side_cell(enemy, sh)} | {clear_cell(enemy, sh)} | {clear_cell(friendly, sh)} |")
    for sh in ():
        fw, ew = friendly[sh][0], enemy[sh][0]
        ce, ue = sh_cost(enemy, sh); cf, uf = sh_cost(friendly, sh)
        md.append(f"| {sh} ({build.STRONGHOLDS[sh]['tier']}) | {fmt(sum(r['power'] for r in friendly[sh]))} · {sum(r['stars'] for r in friendly[sh])}★ · {fw['player']} S{fw['squad']} {fmt(fw['power'])} | {fmt(sum(r['power'] for r in enemy[sh]))} · {sum(r['stars'] for r in enemy[sh])}★ · {ew['player']} S{ew['squad']} {fmt(ew['power'])} | {'never (unkillable squad)' if ue else f'~{ce}'} | {'never (unkillable squad)' if uf else f'~{cf}'} |")
    md += ["", "## Simulation", "", "Same model as our own plan (`sim.py`): path unlocking, win chance rising with power ratio, in-game morale rule, coordinated and greedy attacker behaviours, 8 runs. Columns are attacks landed per squad (each side has 10; sleep and waste push the real number down).", "",
           f"| Attacks landed per squad | 3 | 4 | 5 | 6 | 8 |", "|---|---|---|---|---|---|",
           f"| Stars [{E}] loses when {F} attacks (of {e_stars}) | " + " | ".join(f"{p:.0f} / {g:.0f}" for a, p, g in we_attack) + " |",
           f"| Stars {F} loses when [{E}] attacks (of {f_stars}) | " + " | ".join(f"{p:.0f} / {g:.0f}" for a, p, g in they_attack) + " |",
           "", f"**Verdict: {verdict}** Ceiling for {F}: {ceiling}★ of {e_stars} (the rest sits on unkillable squads).", "",
           "## Attack plan for " + F, "",
           "Rules for every attack: hit only the current phase's stronghold (a half-cleared stronghold unlocks nothing); hit only targets you beat outright — your power ≥ 1.07× theirs at their current morale; a lost attack is only useful as a planned bait; use attempts as they restore (1 per squad every 2 h).", ""]
    for title, desc, squads in ph:
        md += [f"### {title}", "", desc, ""]
        if squads:
            md += ["| Target | SH | Power | ★ | Beat outright by | Est. attacks |", "|---|---|---|---|---|---|"]
            for r in sorted(squads, key=lambda r: (r["sh"], -r["power"])):
                md.append(f"| {r['player']} S{r['squad']}{' (W)' if r['warden'] else ''} | {r['sh']} | {fmt(r['power'])} | {r['stars']} | ≥ {fmt(r['power']*SAFE)} ({r['outright']} of ours) | {r['cost'] if r['cost'] else '—'} |")
            md.append("")
    md += ["## Roles", "", f"| {F} squad | Power | Beats outright up to | Role |", "|---|---|---|---|"]
    for r, beats, role in rl:
        md.append(f"| {r['player']} S{r['squad']} (SH{r['sh']}) | {fmt(r['power'])} | {fmt(beats)} | {role} |")
    (ROOT / "docs" / f"{prefix}.md").write_text("\n".join(md) + "\n", encoding="utf-8")

    # ---------------- html ----------------
    style = build.TEMPLATE[build.TEMPLATE.index("<style>"):build.TEMPLATE.index("</style>") + 8].replace("{{", "{").replace("}}", "}")
    def card(by, sh, who, attackers_label):
        rows_html = []
        for r in by[sh]:
            cls = {"easy": "easy", "mid": "mid", "hard": "hard", "unkillable": "unk"}[r["cls"]]
            note = "unkillable" if r["cls"] == "unkillable" else f"need ≥ {fmt(r['power']*SAFE)} · ~{r['cost']} atk"
            rows_html.append(f'<tr class="{cls}{" warden" if r["warden"] else ""}"><td class="nm">{html.escape(r["player"])} <span class="sq">S{r["squad"]}</span>{" <span class=\"badge\">Warden</span>" if r["warden"] else ""}</td><td class="pw">{fmt(r["power"])}</td><td class="st">{"★"*r["stars"]}</td><td class="mv">{note}</td></tr>')
        info = build.STRONGHOLDS[sh]; c, u = sh_cost(by, sh)
        if not by[sh]:
            return f'<section class="sh tier-{info["tier"].lower()}"><header><h2>{who} Stronghold {sh} <small>{info["tier"]}</small></h2><div class="meta">not scouted — no screenshots</div></header></section>'
        return f'<section class="sh tier-{info["tier"].lower()}"><header><h2>{who} Stronghold {sh} <small>{info["tier"]}</small></h2><div class="meta">{fmt(sum(r["power"] for r in by[sh]))} · {sum(r["stars"] for r in by[sh])}★ · {"cannot be cleared by " + attackers_label if u else f"~{c} attacks for {attackers_label} to clear"}</div></header><table>{"".join(rows_html)}</table></section>'
    def grid(by, who, attackers_label):
        return f'<div class="map">{card(by,4,who,attackers_label)}{card(by,5,who,attackers_label)}{card(by,6,who,attackers_label)}<div class="row2">{card(by,2,who,attackers_label)}{card(by,3,who,attackers_label)}</div><div class="row3">{card(by,1,who,attackers_label)}</div></div>'
    simrows = "".join(f"<tr><td>{a}</td><td>{p:.0f} / {g:.0f}</td><td>{p2:.0f} / {g2:.0f}</td></tr>" for (a, p, g), (_, p2, g2) in zip(we_attack, they_attack))
    phase_html = "".join(f'<div><h3>{html.escape(t)}</h3><p>{html.escape(d)}</p></div>' for t, d, _ in ph)
    roles_html = "".join(f'<tr><td class="nm">{html.escape(r["player"])} <span class="sq">S{r["squad"]} · SH{r["sh"]}</span></td><td class="pw">{fmt(r["power"])}</td><td class="pw">{fmt(beats)}</td><td>{html.escape(role)}</td></tr>' for r, beats, role in rl)
    unk_txt = lambda lst: ", ".join(f"{html.escape(r['player'])} S{r['squad']} {fmt(r['power'])}" for r in lst) or "none"
    page = f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>{html.escape(F)} vs {html.escape(E)} — Winter Siege</title>
{style}
<style>
tr.easy td.mv {{ color:#2e7d32 }} tr.mid td.mv {{ color:#b26a00 }} tr.hard td.mv {{ color:#c0392b }} tr.unk {{ opacity:.5 }}
.rules p {{ margin:0; font-size:13px }} .legend span {{ display:inline-block; margin-right:14px; font-size:12px }}
h2.sect {{ margin:28px 0 8px; font-size:20px }} .cmp td, .cmp th {{ padding:4px 10px; text-align:left }}
</style></head><body><div class="wrap">
<h1>{html.escape(F)} vs [{html.escape(E)}]</h1>
<div class="sub"><b>{html.escape(verdict)}</b>{(" · <span class=\"move\">not scouted: " + html.escape(F) + " Stronghold " + ", ".join(map(str, missing(friendly))) + "</span>") if missing(friendly) else ""}</div>
<div class="rules">
 <div><h3>Who is stronger</h3><table class="cmp"><tr><th></th><th>{html.escape(F)}</th><th>[{html.escape(E)}]</th></tr>
 <tr><td>Garrison power</td><td>{fmt(sum(fpow))}</td><td>{fmt(sum(epow))}</td></tr>
 <tr><td>Squads ≥ 1B / ≥ 2B</td><td>{sum(p>=1e9 for p in fpow)} / {sum(p>=2e9 for p in fpow)}</td><td>{sum(p>=1e9 for p in epow)} / {sum(p>=2e9 for p in epow)}</td></tr>
 <tr><td>Strongest squad</td><td>{fmt(fpow[0])}</td><td>{fmt(epow[0])}</td></tr>
 <tr><td>Layout</td><td>{html.escape(fk)}</td><td>{html.escape(ek)}</td></tr>
 <tr><td>Unkillable by the other side</td><td>{unk_txt(unk_f)}</td><td>{unk_txt(unk_e)}</td></tr></table></div>
 <div><h3>Simulation (stars lost, coordinated / greedy attacker)</h3><table class="cmp"><tr><th>attacks landed per squad</th><th>[{html.escape(E)}] loses (of {e_stars})</th><th>{html.escape(F)} loses (of {f_stars})</th></tr>{simrows}</table>
 <p>Ceiling for {html.escape(F)}: {ceiling}★. Each side has 10 attacks per squad; how many actually land is what decides this.</p></div>
</div>
<h2 class="sect">Their garrisons — what {html.escape(F)} attacks</h2>
<div class="legend"><span style="color:#2e7d32">green = 12+ of {html.escape(F)}'s squads beat it outright</span><span style="color:#b26a00">amber = 3–11 do</span><span style="color:#c0392b">red = needs baiting first</span><span>grey = unkillable</span></div>
{grid(enemy, "Their", F)}
<h2 class="sect">Attack plan for {html.escape(F)}</h2>
<div class="rules">{phase_html}</div>
<h2 class="sect">Our garrisons — what [{html.escape(E)}] attacks</h2>
<div class="legend">colours show how easily <i>they</i> kill each of our squads</div>
{grid(friendly, "Our", E)}
<div class="players"><h2 style="margin:0 0 8px;font-size:18px">Who hits what ({html.escape(F)})</h2><p style="margin:0 0 8px;color:var(--mute)">"Beats outright up to" = their power × current morale you can take without baiting.</p>
<table><tr><td class="nm"><b>Squad</b></td><td class="pw"><b>Power</b></td><td class="pw"><b>Beats up to</b></td><td><b>Role</b></td></tr>{roles_html}</table></div>
</div></body></html>"""
    (ROOT / f"{prefix}.html").write_text(page, encoding="utf-8")
    print(f"{prefix}.html + docs/{prefix}.md — {F} {fmt(sum(fpow))} vs {E} {fmt(sum(epow))}; verdict: {verdict}")


if __name__ == "__main__":
    main()
