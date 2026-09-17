#!/usr/bin/env python3
"""Compare Winter Siege garrison layouts against a simulated enemy.

Rules modelled (in-game Rules Overview, 2026-09-16):
  * unlocking: every squad in a stronghold must be defeated before the strongholds
    it connects to can be attacked. Paths: 4->2, 5->2,3, 6->3, 2->1, 3->1.
  * an attack wins with probability sigmoid(K * ln(attacker / (defender * morale)))
  * defender morale: -10% per defender win above 80%, -5% at/below, floor 60%;
    resets to 100% when the defender loses a Heart (normal 4, Warden 5)
  * the enemy either commits to the cheapest-to-clear reachable stronghold
    ('path', a coordinated alliance) or always hits the best stars-per-expected-
    attack target it can reach ('greedy'); both are reported. It hits with the
    weakest attacker that has >=60% win chance, or baits with its weakest attacker.
  * each enemy squad has N attacks; eliminated squads still attack.
The enemy is our own roster scaled by a power factor.

Usage: python3 sim.py [enemy power factors...]     default: 1.0 1.15 1.3
"""
import copy
import math
import random
import sys
from collections import defaultdict

import build

NEXT = {4: [2], 5: [2, 3], 6: [3], 2: [1], 3: [1], 1: []}
K = 6.0
MORALE_FLOOR = .6
RUNS = 16


def win_prob(attacker, defender_eff):
    return 1 / (1 + math.exp(-K * math.log(attacker / defender_eff)))


def morale_drop(m):
    return max(MORALE_FLOOR, round(m - (.10 if m > .80 else .05), 2))


def exp_cost(d, att):
    """Expected attacks to remove all of d's hearts with the current pool (no depletion)."""
    pool = sorted(a for a, n in att.items() if n > 0)
    if not pool:
        return None
    P = d[0]["power"]; tot = 0
    for _ in range(d[2]):
        m = 1.0; baits = 0
        while not any(win_prob(a, P * m) >= .6 for a in pool):
            if m <= MORALE_FLOOR:
                return None
            m = morale_drop(m); baits += 1
        tot += baits + 1
    return tot


def run(by_sh, enemy, attacks, policy="path", runs=RUNS, rng=random):
    tot = 0
    for _ in range(runs):
        att = defaultdict(int)
        for p in enemy:
            att[p] += attacks
        live = {sh: [[r, sh, 5 if r["warden"] else 4, 1.0] for r in by_sh[sh]] for sh in by_sh}
        cleared = set(); lost = 0; focus = None

        def unlocked():
            u = {4, 5, 6}
            for c in cleared:
                u |= set(NEXT[c])
            return [s for s in u if live[s]]

        while True:
            u = unlocked()
            pool = sorted(a for a, n in att.items() if n > 0)
            if not u or not pool:
                break
            cands = []
            for s in u:  # only the 4 weakest live defenders per stronghold are worth costing
                for d in sorted(live[s], key=lambda x: x[0]["power"] * x[3])[:4]:
                    c = exp_cost(d, att)
                    if c:
                        cands.append((c, d, s))
            if not cands:
                break
            if policy == "greedy":
                c, d, s = min(cands, key=lambda x: -build.stars_for(x[1][0], x[2]) / x[0])
            else:
                if focus not in u or not any(x[2] == focus for x in cands):
                    costs = {}
                    for s in u:
                        cs = [exp_cost(d, att) for d in live[s]]
                        costs[s] = sum(c for c in cs if c) + 1e6 * sum(1 for c in cs if not c)
                    focus = min(costs, key=costs.get)
                inf = [x for x in cands if x[2] == focus] or cands
                c, d, s = min(inf, key=lambda x: x[0])
            need = d[0]["power"] * d[3]
            good = [a for a in pool if win_prob(a, need) >= .6]
            a = good[0] if good else pool[0]
            att[a] -= 1
            if rng.random() < win_prob(a, need):
                d[2] -= 1; d[3] = 1.0
                if d[2] == 0:
                    lost += build.stars_for(d[0], s)
                    live[s].remove(d)
                    if not live[s]:
                        cleared.add(s)
            else:
                d[3] = morale_drop(d[3])
        tot += lost
    return tot / runs


def layout(rows, pools):
    """Balanced layout: pools as in build.POOLS, consumed strongest-first."""
    saved, build.POOLS = build.POOLS, pools
    try:
        return build.assign(rows)
    finally:
        build.POOLS = saved


LAYOUTS = {
    "graded (build.py): 2/3=1-20+69-88, fronts=21-68, 1=89-108": build.POOLS,
    "graded30: 2/3=1-30+79-88, fronts=31-78, 1=89-108": [([2, 3], 15), ([4, 5, 6], 16), ([2, 3], 5), ([1], 20)],
    "vault: 2/3=1-40, fronts=41-88, 1=89-108": [([2, 3], 20), ([4, 5, 6], 16), ([1], 20)],
    "vault+: 2/3=1-40, 1=41-60, fronts=61-108": [([2, 3], 20), ([1], 20), ([4, 5, 6], 16)],
    "core-heavy: 1=1-20, 2/3=21-60, fronts=61-108": [([1], 20), ([2, 3], 20), ([4, 5, 6], 16)],
    "snake 1/2/3=1-60, fronts=61-108": [([1, 2, 3], 20), ([4, 5, 6], 16)],
    "fortress: fronts=1-48, 2/3=49-88, 1=89-108": [([4, 5, 6], 16), ([2, 3], 20), ([1], 20)],
}


def main():
    rows = build.load()
    our = [r["power"] for r in rows]
    budgets = (3, 4, 5, 6)
    factors = [float(x) for x in sys.argv[1:]] or [1.0, 1.15, 1.3]
    print("stars lost of 198, coordinated/greedy attacker, by attacks landed per enemy squad")
    print(f"{'layout':52s}" + "".join(f"  x{f:<4}" + " " * 9 for f in factors))
    for name, pools in LAYOUTS.items():
        by_sh = layout(copy.deepcopy(rows), pools)
        for a in budgets:
            cells = []
            for f in factors:
                enemy = [p * f for p in our]
                random.seed(1); p = run(by_sh, enemy, a, "path")
                random.seed(1); g = run(by_sh, enemy, a, "greedy")
                cells.append(f"  {p:5.0f}/{g:<5.0f}   ")
            print(f"{name[:46]:46s} @{a}   " + "".join(cells))


if __name__ == "__main__":
    main()
