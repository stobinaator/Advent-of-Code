from collections import defaultdict

data = open("input.txt").read().strip()
lines = [x for x in data.split("\n")]

SZ = defaultdict(int)
path = []
RAW = """
$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k""".strip().split("\n")

for line in lines:
    words = line.strip().split()
    
    if words[1] == "cd":
        if words[2] == "..":
            path.pop()
        else:
            path.append(words[2])
    elif words[1] == "ls":
        continue
    elif words[0] == "dir":
        continue
    else:
        sz = int(words[0])
        for i in range(len(path)+1):
            SZ["/".join(path[:i])] += sz

max_used = 70_000_000 - 30_000_000
total_used = SZ["/"] # 2_476_859
need_to_free = total_used - max_used

p1 = 0
p2 = 1e9
for k,v in SZ.items():
    if v <= 100_000:
        p1 += v
    if v >= need_to_free:
        p2 = min(p2, v)
print(p1)
print(p2)
