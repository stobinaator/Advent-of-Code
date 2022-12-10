import os

cd = os.path.abspath(os.getcwd())
data = open(f"{cd}/input.txt").read().strip()

G = []
for line in data.split("\n"):
    assert line.strip() == line
    G.append(line)

R = len(G)
C = len(G[0])

t = 0
while True:
    t += 1
    moved = False
    G2 = [[G[r][c] for c in range(C)] for r in range(R)]
    for r in range(R):
        for c in range(C):
            if G[r][c] == ">" and G[r][(c + 1) % C] == ".":
                moved = True
                G2[r][(c + 1) % C] = ">"
                G2[r][c] = "."

    G3 = [[G2[r][c] for c in range(C)] for r in range(R)]
    for r in range(R):
        for c in range(C):
            if G2[r][c] == "v" and G2[(r + 1) % R][c] == ".":
                moved = True
                G3[(r + 1) % R][c] = "v"
                G3[r][c] = "."
    if not moved:
        print(t)
        break
    G = G3
