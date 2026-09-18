#!/usr/bin/env python3
"""Generate battle.html and docs/battle-plan.md from data/enemy.csv (scouted
enemy garrisons) and data/squads.csv (our roster).

Kill model (see sim.py): an attack is a safe win when attacker power is at
least SAFE x the defender's effective power (power x morale). Morale floor is
60%, so a defender is unkillable for us if 0.6 x its power x SAFE exceeds our
strongest squad. Bait = a deliberately lost attack that drops the defender's
morale (-10% above 80%, -5% at or below, floor 60%).
"""
import csv
import html
from collections import defaultdict
from pathlib import Path

import build

ROOT = Path(__file__).parent
SAFE = 1.07          # attacker/defender ratio for a ~60%+ win in the model
FLOOR = 0.6
NEXT = {4: [2], 5: [2, 3], 6: [3], 2: [1], 3: [1], 1: []}


def load_enemy():
    rows = list(csv.DictReader(open(ROOT / "data" / "enemy.csv", encoding="utf-8")))
    by = defaultdict(list)
    for r in rows:
        r["power"] = int(r["power"]); r["sh"] = int(r["stronghold"])
        r["warden"] = r["warden"] == "1"; r["hearts"] = 5 if r["warden"] else 4
        by[r["sh"]].append(r)
    for l in by.values():
        l.sort(key=lambda r: -r["power"])
    return rows, by


def baits_needed(defender, attacker):
    """Defender wins needed before `attacker` gets a safe hit; None if never."""
    m, n = 1.0, 0
    while attacker < defender * m * SAFE:
        if m <= FLOOR:
            return None
        m = max(FLOOR, round(m - (.10 if m > .80 else .05), 2)); n += 1
    return n


def fmt(n):
    return f"{n/1e9:.2f}B" if n >= 1e9 else f"{n/1e6:.0f}M"


def classify(r, our):
    """Cost class for one enemy squad against our roster."""
    best = our[0]
    b = baits_needed(r["power"], best)
    if b is None:
        return "unkillable", None, 0
    # cheapest: how many of our squads beat it outright at 100% morale
    outright = sum(p >= r["power"] * SAFE for p in our)
    if outright >= 12:
        cls = "easy"
    elif outright >= 3:
        cls = "mid"
    else:
        cls = "hard"
    # expected attacks: per heart, baits until >=3 of our squads qualify (so it
    # isn't gated on one player's 10 attempts), plus the kill
    m, baits = 1.0, 0
    while sum(p >= r["power"] * m * SAFE for p in our) < 3:
        if m <= FLOOR:
            break
        m = max(FLOOR, round(m - (.10 if m > .80 else .05), 2)); baits += 1
    cost = r["hearts"] * (baits + 1)
    return cls, outright, cost


def main():
    enemy, eby = load_enemy()
    ours = build.load()
    our = sorted((r["power"] for r in ours), reverse=True)
    for r in enemy:
        r["cls"], r["outright"], r["cost"] = classify(r, our)
        r["stars"] = build.STRONGHOLDS[r["sh"]]["stars"] * (2 if r["warden"] else 1)

    their_total = sum(r["power"] for r in enemy)
    stars_total = sum(r["stars"] for r in enemy)
    unkillable = [r for r in enemy if r["cls"] == "unkillable"]

    # ---- phases -------------------------------------------------------------
    def sh_cost(sh):
        return sum(r["cost"] for r in eby[sh])
    fronts = sorted((4, 5, 6), key=sh_cost)
    cheap_adv = [r for sh in (2, 3) for r in eby[sh] if r["cls"] == "easy"]
    mid_adv = [r for sh in (2, 3) for r in eby[sh] if r["cls"] == "mid"]
    hard_adv = [r for sh in (2, 3) for r in eby[sh] if r["cls"] == "hard"]
    phases = [
        ("Phase 1 — open the map: clear Stronghold 5",
         f"Their weakest Warden (jinx S1, {fmt(eby[5][0]['power'])}, 5 Hearts) and it unlocks BOTH 2 and 3. "
         f"About {sh_cost(5)} attacks for 21★. Mid squads (500–800M) take the rank 2–10 squads; anything under 400M is a job for our 450–600M squads. "
         f"The Warden needs attackers over {fmt(eby[5][0]['power']*SAFE)} — no baiting needed, we have plenty.",
         eby[5]),
        ("Phase 2 — farm the cheap 2★ squads in Strongholds 2 and 3",
         f"{len(cheap_adv)} squads worth 2★ each that 12+ of our squads beat outright: ~{sum(r['cost'] for r in cheap_adv)} attacks for {2*len(cheap_adv)}★. "
         "This is the best Stars-per-attack on their board. Do NOT waste attacks on their whales here yet.",
         cheap_adv),
        ("Phase 3 — clear Strongholds 4 and 6",
         f"About {sh_cost(4)} + {sh_cost(6)} attacks for 42★. Same squad tiers as Phase 1. Wardens Macsen S2 ({fmt(eby[4][0]['power'])}) and Mistyy S1 ({fmt(eby[6][0]['power'])}) need attackers over {fmt(eby[4][0]['power']*SAFE)}.",
         eby[4] + eby[6]),
        ("Phase 4 — mid 2★ targets in 2 and 3",
         f"{len(mid_adv)} squads that 3–11 of our squads beat outright, or that need a bait or two first: ~{sum(r['cost'] for r in mid_adv)} attacks for {2*len(mid_adv)}★.",
         mid_adv),
        ("Phase 5 — only if attacks are left: the hard 2★ targets",
         f"{len(hard_adv)} squads that need 4–6 baits per Heart before one of our top squads can finish: ~{sum(r['cost'] for r in hard_adv)} attacks for {2*len(hard_adv)}★. "
         "Poor value; do it with leftover attempts. NoSoup4u S2 (their SH3 Warden) can only be finished by Leoder S1 at 60% morale and is what stands between us and their Stronghold 1 — not worth it.",
         hard_adv),
    ]
    ceiling = stars_total - sum(r["stars"] for r in unkillable)

    # ---- member guide -------------------------------------------------------
    roles = []
    for r in sorted(ours, key=lambda r: -r["power"]):
        p = r["power"]; beats = p / SAFE
        if p >= 1.0e9:
            role = "Finisher — save attacks for Phase 4/5 targets after they've been baited; don't spend them on fronts"
        elif p >= 7.0e8:
            role = "Heavy hitter — front Wardens and the 600–750M squads"
        elif p >= 4.5e8:
            role = "Line hitter — fronts (Phase 1/3) and cheap 2★ squads (Phase 2)"
        else:
            role = "Baiter / cleanup — squads under your threshold, and bait duty on whales when called"
        roles.append((r, beats, role))

    # ---- markdown -----------------------------------------------------------
    md = [f"# Battle plan vs [AoA]", "",
          f"Scouted 2026-09-17. Their garrison: **{fmt(their_total)}** across 120 squads ({sum(p>=1e9 for p in (r['power'] for r in enemy))} over 1B, {sum(p>=2e9 for p in (r['power'] for r in enemy))} over 2B). Ours: {fmt(sum(our))} across {len(our)} squads ({sum(p>=1e9 for p in our)} over 1B, none over 2B).", "",
          "## The honest picture", "",
          "- Their layout is the opposite of ours: whales in Stronghold 1 (19.9B), strong 2/3 (14.7B / 14.8B), weak fronts (7.5–8.7B).",
          f"- Two of their squads are unkillable for us even at the 60% morale floor: {', '.join(f'{r['player']} S{r['squad']} ({fmt(r['power'])}, {r['stars']}★)' for r in unkillable)}. So we can never zero them; our ceiling is {ceiling}★ and the realistic haul with a full day of attacks is about 130–140★.",
          "- Their top squads beat every squad we have without baiting, so on defence we can only make them spend attacks. The simulation says they take ~110★ from us if they land 3 attacks per squad, ~170★ at 5, and wipe us at 8 — so **the result depends on how active they are, not on anything we can still change.**",
          "- Our win condition is therefore: **take Stars faster than they do and hope they're less active.** Every unused attack of ours is a Star we didn't take.", "",
          "## Target order", ""]
    for title, desc, squads in phases:
        md.append(f"### {title}"); md.append(""); md.append(desc); md.append("")
        md.append("| Target | Stronghold | Power | Stars | Beat outright by | Est. attacks |")
        md.append("|---|---|---|---|---|---|")
        for r in sorted(squads, key=lambda r: (r["sh"], -r["power"])):
            md.append(f"| {r['player']} S{r['squad']}{' (W)' if r['warden'] else ''} | {r['sh']} | {fmt(r['power'])} | {r['stars']} | our squads ≥ {fmt(r['power']*SAFE)} ({r['outright']}) | {r['cost']} |")
        md.append("")
    md += ["## Rules of engagement", "",
           "- Attack only the current phase's stronghold unless told otherwise; a half-cleared stronghold unlocks nothing.",
           "- Pick targets you beat **outright** (your power ≥ 1.07× theirs at their current morale). A lost attack is only useful when it's a planned bait.",
           "- Baiting: a defender's stats drop 10% per win above 80%, then 5%, floor 60%. Losing a Heart resets it. So bait a whale down, then finish, then repeat per Heart — never finish before the baits are in.",
           "- Attacks restore 1 per squad every 2 hours (max 7 restored). Use them as they come; unused attacks at the end are wasted Stars.",
           "- Their SH1 is out of reach. Don't plan around it.", "",
           "## Who hits what", "", "Your safe target is anything at or below the threshold (their power × current morale). Finishers: keep your attempts for the baited whales.", "",
           "| Our squad | Power | Beats outright up to | Role |", "|---|---|---|---|"]
    for r, beats, role in roles:
        md.append(f"| {r['player']} S{r['squad']} | {fmt(r['power'])} | {fmt(beats)} | {role} |")
    (ROOT / "docs" / "battle-plan.md").write_text("\n".join(md) + "\n", encoding="utf-8")

    # ---- html ---------------------------------------------------------------
    style = build.TEMPLATE[build.TEMPLATE.index("<style>"):build.TEMPLATE.index("</style>") + 8].replace("{{", "{").replace("}}", "}")
    def card(sh):
        rows_html = []
        for r in eby[sh]:
            cls = {"easy": "easy", "mid": "mid", "hard": "hard", "unkillable": "unk"}[r["cls"]]
            rows_html.append(f'<tr class="{cls}{" warden" if r["warden"] else ""}"><td class="nm">{html.escape(r["player"])} <span class="sq">S{r["squad"]}</span>{" <span class=\"badge\">Warden</span>" if r["warden"] else ""}</td>'
                             f'<td class="pw">{fmt(r["power"])}</td><td class="st">{"★"*r["stars"]}</td>'
                             f'<td class="mv">{"unkillable" if r["cls"]=="unkillable" else f"need ≥ {fmt(r["power"]*SAFE)} · ~{r["cost"]} atk"}</td></tr>')
        info = build.STRONGHOLDS[sh]
        return f'<section class="sh tier-{info["tier"].lower()}"><header><h2>Their Stronghold {sh} <small>{info["tier"]}</small></h2><div class="meta">{fmt(sum(r["power"] for r in eby[sh]))} · {sum(r["stars"] for r in eby[sh])}★ · ~{sh_cost(sh)} attacks to clear</div></header><table>{"".join(rows_html)}</table></section>'
    phase_html = "".join(f'<div><h3>{html.escape(t)}</h3><p>{html.escape(d)}</p></div>' for t, d, _ in phases)
    roles_html = "".join(f'<tr><td class="nm">{html.escape(r["player"])} <span class="sq">S{r["squad"]}</span></td><td class="pw">{fmt(r["power"])}</td><td class="pw">{fmt(beats)}</td><td>{html.escape(role)}</td></tr>' for r, beats, role in roles)
    page = f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>Winter Siege Battle Plan</title>
{style}
<style>
tr.easy td.mv {{ color:#2e7d32 }} tr.mid td.mv {{ color:#b26a00 }} tr.hard td.mv {{ color:#c0392b }} tr.unk {{ opacity:.5 }}
.rules p {{ margin:0; font-size:13px }}
.legend span {{ display:inline-block; margin-right:14px; font-size:12px }}
</style></head><body><div class="wrap">
<h1>Battle plan vs [AoA]</h1>
<div class="sub">Their garrison {fmt(their_total)} vs ours {fmt(sum(our))} · they have {sum(p>=1e9 for p in (r['power'] for r in enemy))} squads over 1B (we have {sum(p>=1e9 for p in our)}) · two of theirs are unkillable · our ceiling {ceiling}★, realistic 130–140★ · <b>our win condition: out-attack them</b></div>
<div class="legend"><span style="color:#2e7d32">green = 12+ of our squads beat it outright</span><span style="color:#b26a00">amber = 3–11 do</span><span style="color:#c0392b">red = needs baiting first</span><span>grey = unkillable</span></div>
<div class="map">{card(4)}{card(5)}{card(6)}<div class="arrows">Clear 5 first: it opens both 2 and 3. Their 1 is behind two unkillable-or-nearly squads — ignore it.</div><div class="row2">{card(2)}{card(3)}</div><div class="row3">{card(1)}</div></div>
<div class="rules">{phase_html}</div>
<div class="players"><h2 style="margin:0 0 8px;font-size:18px">Who hits what</h2><p style="margin:0 0 8px;color:var(--mute)">"Beats outright up to" = their power × current morale you can take without baiting. Finishers keep attempts for baited whales.</p>
<table><tr><td class="nm"><b>Squad</b></td><td class="pw"><b>Power</b></td><td class="pw"><b>Beats up to</b></td><td><b>Role</b></td></tr>{roles_html}</table></div>
</div></body></html>"""
    (ROOT / "battle.html").write_text(page, encoding="utf-8")
    print(f"battle.html + docs/battle-plan.md: ceiling {ceiling}★, phases " + ", ".join(str(len(s)) for _, _, s in phases))


if __name__ == "__main__":
    main()
