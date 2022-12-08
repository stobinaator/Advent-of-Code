lines = [x for x in open("input.txt").read().strip().split("\n")]

G = []
for line in lines:
    row = line
    G.append(row)

DIR = [(-1,0),(0,1),(1,0),(0,-1)]
R = len(G)
C = len(G[0])

pt1 = 0

for r in range(R):
    for c in range(C):
        vis = False
        for (dr, dc) in DIR:
            rr = r
            cc = c
            not_ok = True
            while True:
                rr += dr
                cc += dc
                if not (0<=rr<R and 0<=cc<C):
                    break
                if G[rr][cc] >= G[r][c]:
                    not_ok = False
            if not_ok:
                vis = True
        if vis:
            pt1 +=1

print(pt1)

pt2 = 0

for r in range(R):
    for c in range(C):
        score = 1
        for (dr, dc) in DIR:
            distance = 1
            rr = r+dr
            cc = c+dc
            while True:
                if not (0<=rr<R and 0<=cc<C):
                    distance -= 1
                    break
                if G[rr][cc] >= G[r][c]:
                    break
                distance += 1    
                rr += dr
                cc += dc
            score *= distance
        pt2 = max(pt2, score)

print(pt2)