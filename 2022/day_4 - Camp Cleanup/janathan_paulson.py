lines = [sections for sections in open("input.txt").read().strip().split("\n")]

p1 = 0
p2 = 0
for line in lines:
    one, two = line.split(",")
    s1, e1 = one.split("-")
    s2, e2 = two.split("-")
    s1, e1, s2, e2 = [int(x) for x in [s1, e1, s2, e2]]
    # (s2, e2) is fully contained in (s1, e1) if s1<=s2 and e2<=e1
    if s1 <= s2 and e2 <= e1 or s2 <= s1 and e1 <= e2:
        p1 += 1
    # (s2, e2) overlaps (s1, e1) if it is not completely to the left or completely to the right
    if not (e2 < s1 or e1 < s2): # not (e1 < s2 or s1 > e2)
        p2 += 1
print(p1)
print(p2)