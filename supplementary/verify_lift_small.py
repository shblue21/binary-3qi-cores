#!/usr/bin/env python3
"""Finite falsification checks for the middle-layer lift."""

from itertools import combinations


class VerificationError(RuntimeError):
    """Raised when a finite lift check fails."""


def require(condition, message):
    if not condition:
        raise VerificationError(message)


def popcount(value):
    return bin(value).count("1")


def vertices(n):
    out = []
    for size in range(4, n - 3):
        for rest in combinations(range(1, n), size - 1):
            mask = 1
            for point in rest:
                mask |= 1 << point
            out.append(mask)
    return out


def blocks(mask, n):
    full = (1 << n) - 1
    return mask, full ^ mask


def edge3(a, b, c, n):
    full = (1 << n) - 1
    choices = ((a, full ^ a), (b, full ^ b), (c, full ^ c))
    for x in choices[0]:
        for y in choices[1]:
            for z in choices[2]:
                if x & y & z == 0:
                    return False
    return True


def middle(mask, n):
    size = popcount(mask)
    return min(size, n - size) == n // 2


def separation_witness(x, y, n):
    full = (1 << n) - 1
    x_blocks = blocks(x, n)
    y_blocks = blocks(y, n)
    chosen_e = None
    for candidate in y_blocks:
        if all(candidate & x_block for x_block in x_blocks):
            chosen_e = candidate
            break
    require(chosen_e is not None,
            "no separating Y-block meets both blocks of X")

    colours = [-1] * n
    for x_block in x_blocks:
        inside_e = [p for p in range(n) if (x_block >> p) & 1 and
                    (chosen_e >> p) & 1]
        require(inside_e, "chosen Y-block misses a block of X")
        colours[inside_e[0]] = 3
        remaining = [p for p in range(n) if (x_block >> p) & 1 and
                     colours[p] < 0]
        require(len(remaining) >= 3,
                "an X-block has fewer than three uncoloured points")
        colours[remaining[0]] = 0
        colours[remaining[1]] = 1
        colours[remaining[2]] = 2

    k = n // 2
    target = [2, k - 2, k - 2, 2] if n % 2 == 0 else [3, k - 2, k - 2, 2]
    current = [colours.count(colour) for colour in range(4)]
    deficit = [target[i] - current[i] for i in range(4)]
    require(all(value >= 0 for value in deficit),
            "target colour multiplicities do not dominate the seed")
    uncoloured = [p for p in range(n) if colours[p] < 0]
    require(sum(deficit) == len(uncoloured),
            "colour deficit does not match the uncoloured points")
    cursor = 0
    for colour, count in enumerate(deficit):
        for _ in range(count):
            colours[uncoloured[cursor]] = colour
            cursor += 1

    r = 0
    s = 0
    for point, colour in enumerate(colours):
        if colour in (2, 3):
            r |= 1 << point
        if colour in (1, 3):
            s |= 1 << point
    require(middle(r, n) and middle(s, n),
            "constructed anchors are not in the middle layer")
    require(r != s and r != (full ^ s),
            "constructed anchors represent the same bipartition")
    require(edge3(x, r, s, n),
            "constructed anchors do not form an edge with X")
    require(not edge3(y, r, s, n),
            "constructed anchors also form an edge with Y")
    return r, s


def cross_graph(t):
    verts = []
    for size in range(1, t):
        for rest in combinations(range(1, t), size - 1):
            mask = 1
            for point in rest:
                mask |= 1 << point
            verts.append(mask)
    full = (1 << t) - 1
    adjacency = [0] * len(verts)
    for i, a in enumerate(verts):
        for j in range(i + 1, len(verts)):
            b = verts[j]
            cells = (a & b, a & (full ^ b), (full ^ a) & b,
                     (full ^ a) & (full ^ b))
            if all(cells):
                adjacency[i] |= 1 << j
                adjacency[j] |= 1 << i
    return adjacency


def maximum_clique(adjacency):
    best = [0]

    def expand(size, candidates):
        if size + popcount(candidates) <= best[0]:
            return
        if not candidates:
            best[0] = max(best[0], size)
            return
        while candidates:
            vertex_bit = candidates & -candidates
            vertex = vertex_bit.bit_length() - 1
            candidates ^= vertex_bit
            expand(size + 1, candidates & adjacency[vertex])
        best[0] = max(best[0], size)

    expand(0, (1 << len(adjacency)) - 1)
    return best[0]


def main():
    expected_q = {4: 3, 5: 4, 6: 10}
    for t, expected in expected_q.items():
        actual = maximum_clique(cross_graph(t))
        require(actual == expected,
                "q({}) is {}, expected {}".format(t, actual, expected))
        print("Q({})={}".format(t, actual))

    for n in (8, 9, 10):
        verts = vertices(n)
        checks = 0
        for x in verts:
            for y in verts:
                if x == y:
                    continue
                separation_witness(x, y, n)
                checks += 1
        print("N{}_ORDERED_SEPARATION_CHECKS={}".format(n, checks))
    print("LIFT_SMALL_CHECKS_OK")


if __name__ == "__main__":
    main()
