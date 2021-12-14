import os
from collections import Counter

cd = os.path.abspath(os.getcwd())

RAW = """NNCB

CH -> B
HH -> N
CB -> H
NH -> C
HB -> C
HC -> B
HN -> C
NN -> C
BH -> H
NC -> B
NB -> B
BN -> B
BB -> N
BC -> B
CC -> N
CN -> C"""




tpl, _, *rules = open(f'{cd}/input.txt').read().split('\n')
#tpl, _, *rules = RAW.split('\n')
rules = dict(r.split(" -> ") for r in rules if r!="")
pairs = Counter(map(str.__add__, tpl, tpl[1:]))
chars = Counter(tpl)

for _ in range(40):
    for (a,b), c in pairs.copy().items():
        x = rules[a+b]
        pairs[a+b] -= c
        pairs[a+x] += c
        pairs[x+b] += c
        chars[x] += c

print(max(chars.values())-min(chars.values()))
