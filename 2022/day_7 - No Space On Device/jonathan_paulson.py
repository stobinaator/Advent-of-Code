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
    else:
        try:
            sz = int(words[0])
            for i in range(len(path)+1):
                SZ["/".join(path[:i])] += sz
        except:
            pass

max_used = 70_000_000 - 30_000_000
total_used = SZ["/"] # 2_476_859
need_to_free = total_used - max_used

best = 1e9
ans = 0
for k,v in SZ.items():
    if v >= need_to_free:
        best = min(best, v)
    if v <= 100_000:
        ans += v
print(ans)
print(best)
