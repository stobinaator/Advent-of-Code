import os

cd = os.path.abspath(os.getcwd())

rule, start = open(f"{cd}/input.txt").read().split("\n\n")
rule = rule.strip()
assert len(rule) == 512

G = set()
for r, line in enumerate(start.strip().split("\n")):
    for c, x in enumerate(line.strip()):
        if x == "#":
            G.add((r, c))

# on=true means G says what pixels are on (all the rest are off).
# on=false means G says what pixels are *off* (all the rest are on)
def step(G, on):
    G2 = set()
    rlo = min(r for r, _ in G)
    rhi = max(r for r, _ in G)
    clo = min(c for _, c in G)
    chi = max(c for _, c in G)
    for r in range(rlo - 5, rhi + 10):
        for c in range(clo - 5, chi + 10):
            rc_str = 0
            bit = 8
            for dr in [-1, 0, 1]:
                for dc in [-1, 0, 1]:
                    if ((r + dr, c + dc) in G) != on:
                        rc_str += 2 ** bit
                    bit -= 1
            assert 0 <= rc_str < 512
            if (rule[rc_str] == "#") == on:
                G2.add((r, c))
    return G2


# part1
# G2 = step(G, False)
# G3 = step(G2, True)
# print(len(G3))

# part2
for t in range(50):
    G = step(G, t % 2 == 1)
print(len(G))
