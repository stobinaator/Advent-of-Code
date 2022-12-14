data =  open("input.txt").read().strip()


RAW = """[1,1,3,1,1]
[1,1,5,1,1]

[[1],[2,3,4]]
[[1],4]

[9]
[[8,7,6]]

[[4,4],4,4]
[[4,4],4,4,4]

[7,7,7,7]
[7,7,7]

[]
[3]

[[[]]]
[[]]

[1,[2,[3,[4,[5,6,7]]]],8,9]
[1,[2,[3,[4,[5,6,0]]]],8,9]"""



def compare(p1, p2):
    if isinstance(p1, int) and isinstance(p2, int):
        if p1 < p2:
            return -1
        elif p1 == p2:
            return 0
        else:
            return 1
    elif isinstance(p1, list) and isinstance(p2, list):
        i = 0
        while i<len(p1) and i<len(p2):
            c = compare(p1[i], p2[i])
            if c == -1:
                return -1
            if c == 1:
                return 1
            i += 1
        if i == len(p1) and i < len(p2):
            return -1
        elif i == len(p2) and i < len(p1):
            return 1
        else:
            return 0
    elif isinstance(p1, int) and isinstance(p2, list):
       return compare([p1], p2)
    else:
        return compare(p1, [p2])




packets = []
part1 = 0

for i, group in enumerate(data.split("\n\n")):
    p1, p2 = group.split("\n")
    p1 = eval(p1)
    p2 = eval(p2)
    packets.append(p1)
    packets.append(p2)
    if compare(p1, p2) == -1:
        part1 += 1+i
print(part1)

packets.append([[2]])
packets.append([[6]])
from functools import cmp_to_key
packets = sorted(packets, key=cmp_to_key(lambda p1,p2: compare(p1, p2)))
part2 = 1
for i, p in enumerate(packets):
    if p == [[2]] or p == [[6]]:
        part2 *= i + 1
print(part2)
