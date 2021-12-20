# target area: x=20..30, y=-10..-5
# target area: x=150..171, y=-129..-70

p2 = 0
ans = 0
for DX in range(171):
    for DY in range(-135, 1000):
        ok = False
        max_y = 0
        x = 0
        y = 0
        dx = DX
        dy = DY
        for t in range(1000):
            x += dx
            y += dy
            max_y = max(max_y, y)
            if dx > 0:
                dx -= 1
            elif dx < 0:
                dx += 1
            dy -= 1

            # if 20<=x<=30 and -10<=y<=-5:
            if 150 <= x <= 171 and -129 <= y <= -70:
                ok = True
        if ok:
            p2 += 1
            ans = max(max_y, y)
print(ans)
print(p2)
