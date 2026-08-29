#!/usr/bin/env python3
"""Verify the n=12 and n=16 critical-fold certificates."""

from itertools import combinations, product
from math import comb


def finite_atoms(ground, triple):
    out = []
    for bits in product((0, 1), repeat=3):
        cell = set(ground)
        for block, bit in zip(triple, bits):
            cell &= block if bit else set(ground) - block
        out.append(len(cell))
    return tuple(out)


def seven_cell_edge(ground, a, b, c):
    return all(finite_atoms(ground, (a, b, c))[:-1])


def verify_n12():
    ground = set(range(11))
    p = {0, 1, 2, 3, 4}
    q = {0, 1, 2, 3, 5}
    aux = [
        {1, 2, 3, 5, 10},
        {0, 3, 8, 9, 10},
        {0, 2, 7, 9, 10},
        {2, 3, 4, 9, 10},
        {1, 3, 4, 8, 10},
        {1, 2, 4, 7, 10},
        {0, 5, 7, 8, 9},
        {0, 1, 6, 7, 10},
        {3, 4, 5, 7, 9},
        {2, 4, 5, 6, 9},
        {1, 4, 5, 7, 8},
    ]
    rows = {
        0: "PPPPPPPPPP",
        1: "PQQQQPPPP",
        2: "QQQQPPPP",
        3: "PPPQQQQ",
        4: "PPPQQQ",
        5: "PQPQQ",
        6: "QQPQ",
        7: "PPP",
        8: "PP",
        9: "P",
    }
    checks = 0
    for i, entries in rows.items():
        for offset, symbol in enumerate(entries, start=1):
            j = i + offset
            anchor = p if symbol == "P" else q
            assert seven_cell_edge(ground, anchor, aux[i], aux[j])
            checks += 1
    assert checks == 55
    return checks


def complement_pair_key(block, ground):
    comp = frozenset(ground - set(block))
    block = frozenset(block)
    return min(tuple(sorted(block)), tuple(sorted(comp)))


def verify_m4():
    m = 4
    kset = set(range(0, 2 * m - 2))
    p, q = 2 * m - 2, 2 * m - 1
    wset = set(range(2 * m, 4 * m - 1))
    ground = kset | {p, q} | wset
    x = min(kset)
    u, v = sorted(wset)[:2]
    p_block = kset | {p}
    q_block = kset | {q}
    outside_q = {p} | wset

    d_classes = {0: [], 10: [], 11: []}
    for block in combinations(sorted(q_block), m - 1):
        block = frozenset(block)
        if x not in block:
            kind = 0
        elif q not in block:
            kind = 10
        else:
            kind = 11
        d_classes[kind].append(block)

    pair_classes = {0: [], 10: [], 11: []}
    seen = set()
    for block in combinations(sorted(outside_q), m):
        key = complement_pair_key(block, outside_q)
        if key in seen:
            continue
        seen.add(key)
        first = frozenset(key)
        second = frozenset(outside_q - set(first))
        if (u in first) != (v in first):
            kind = 0
            representatives = (first, second)
        else:
            p_free = first if p not in first else second
            if u in p_free and v in p_free:
                kind = 10
            elif u not in p_free and v not in p_free:
                kind = 11
            else:
                raise AssertionError("unclassified complement pair")
            representatives = (p_free,)
        pair_classes[kind].append((key, representatives))

    expected = {
        0: comb(2 * m - 2, m - 1),
        10: comb(2 * m - 3, m - 2),
        11: comb(2 * m - 3, m - 3),
    }
    assert {kind: len(items) for kind, items in d_classes.items()} == expected
    assert {kind: len(items) for kind, items in pair_classes.items()} == expected

    central = []
    central_kind = []
    for kind in (0, 10, 11):
        left = sorted(d_classes[kind], key=lambda z: tuple(sorted(z)))
        right = sorted(pair_classes[kind], key=lambda z: z[0])
        for index, (a, (_, representatives)) in enumerate(zip(left, right)):
            b = representatives[index % len(representatives)]
            central.append(frozenset(set(a) | set(b)))
            central_kind.append(kind)

    assert len(central) == comb(2 * m - 1, m - 1) == 35
    assert len(set(central)) == len(central)
    assert all(len(block) == 2 * m - 1 for block in central)

    exceptional = frozenset({x, p} | (wset - {u, v}))
    assert len(exceptional) == 2 * m - 1
    assert exceptional not in central

    central_checks = 0
    for i, j in combinations(range(len(central)), 2):
        assert seven_cell_edge(ground, q_block, central[i], central[j])
        central_checks += 1

    exceptional_checks = 0
    for block, kind in zip(central, central_kind):
        anchor = q_block if kind == 0 else p_block
        assert seven_cell_edge(ground, anchor, exceptional, block)
        exceptional_checks += 1

    assert central_checks == 595
    assert exceptional_checks == 35
    return central_checks, exceptional_checks


def main():
    n12 = verify_n12()
    central, exceptional = verify_m4()
    print("N12_ANCHOR_CHECKS={}".format(n12))
    print("M4_CENTRAL_CHECKS={}".format(central))
    print("M4_EXCEPTIONAL_CHECKS={}".format(exceptional))
    print("TOTAL_CHECKS={}".format(n12 + central + exceptional))
    print("CERTIFICATES_OK")


if __name__ == "__main__":
    main()
