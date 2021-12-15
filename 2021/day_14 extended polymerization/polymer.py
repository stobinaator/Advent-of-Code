"""
--- Day 14: Extended Polymerization ---
The incredible pressures at this depth are starting to put a strain on your submarine. The submarine has polymerization equipment that would produce suitable materials to reinforce the submarine, and the nearby volcanically-active caves should even have the necessary input elements in sufficient quantities.

The submarine manual contains instructions for finding the optimal polymer formula; specifically, it offers a polymer template and a list of pair insertion rules (your puzzle input). You just need to work out what polymer would result after repeating the pair insertion process a few times.

For example:

NNCB

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
CN -> C
The first line is the polymer template - this is the starting point of the process.

The following section defines the pair insertion rules. A rule like AB -> C means that when elements A and B are immediately adjacent, element C should be inserted between them. These insertions all happen simultaneously.

So, starting with the polymer template NNCB, the first step simultaneously considers all three pairs:

The first pair (NN) matches the rule NN -> C, so element C is inserted between the first N and the second N.
The second pair (NC) matches the rule NC -> B, so element B is inserted between the N and the C.
The third pair (CB) matches the rule CB -> H, so element H is inserted between the C and the B.
Note that these pairs overlap: the second element of one pair is the first element of the next pair. Also, because all pairs are considered simultaneously, inserted elements are not considered to be part of a pair until the next step.

After the first step of this process, the polymer becomes NCNBCHB.

Here are the results of a few steps using the above rules:

Template:     NNCB
After step 1: NCNBCHB
After step 2: NBCCNBBBCBHCB
After step 3: NBBBCNCCNBBNBNBBCHBHHBCHB
After step 4: NBBNBNBBCCNBCNCCNBBNBBNBBBNBBNBBCBHCBHHNHCBBCBHCB
This polymer grows quickly. After step 5, it has length 97; After step 10, it has length 3073. After step 10, B occurs 1749 times, C occurs 298 times, H occurs 161 times, and N occurs 865 times; taking the quantity of the most common element (B, 1749) and subtracting the quantity of the least common element (H, 161) produces 1749 - 161 = 1588.

Apply 10 steps of pair insertion to the polymer template and find the most and least common elements in the result. What do you get if you take the quantity of the most common element and subtract the quantity of the least common element?
2010

-- Part Two ---
The resulting polymer isn't nearly strong enough to reinforce the submarine. You'll need to run more steps of the pair insertion process; a total of 40 steps should do it.

In the above example, the most common element is B (occurring 2192039569602 times) and the least common element is H (occurring 3849876073 times); subtracting these produces 2188189693529.

Apply 40 steps of pair insertion to the polymer template and find the most and least common elements in the result. What do you get if you take the quantity of the most common element and subtract the quantity of the least common element?
2437698971143
"""
from typing import Dict, List, Counter
import os

cd = os.path.abspath(os.getcwd())

class Polymer:
    def __init__(self, instructions: Dict[str, str], template: str) -> None:
        self.instructions = instructions
        self.template = template
        self.matches = List

    def polymerization(self) -> None:
        self.template = list(self.template)
         
        self.matches = [self.instructions.get(c1+c2) for c1, c2 in zip(self.template, self.template[1:])]
        [self.template.insert(i+i+1, cha) for i, cha in enumerate(self.matches)]
        self.template = "".join(cha for cha in self.template)

    def step(self, times: int) -> List[str]:
        for _ in range(times):
            self.polymerization()
        return self.template

    def result(self) -> int:
        ctr= Counter(self.template)
        return max(ctr.values()) - min(ctr.values())
        
    def parse(raw: str) -> 'Polymer':
        templ, instructions = raw.split("\n\n")
        instructions = [instr.strip() for instr in instructions.splitlines()]
        # why is it not working?
        #instructions_dict = dict(instr.split(' ->') for instr in instructions)
        instructions_dict = dict()
        for instr in instructions:
            one, two = instr.split(' -> ')
            instructions_dict[one] = two

        return Polymer(instructions_dict, templ)

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


POLY = Polymer.parse(RAW)

POLY.step(1)
assert POLY.template == "NCNBCHB"
POLY.step(1)
assert POLY.template == "NBCCNBBBCBHCB"
POLY.step(1)
assert POLY.template == "NBBBCNCCNBBNBNBBCHBHHBCHB"
POLY.step(1)
assert POLY.template == "NBBNBNBBCCNBCNCCNBBNBBNBBBNBBNBBCBHCBHHNHCBBCBHCB"

POLY.step(6)
assert POLY.result() == 1588
#POLY.step(30)
#assert POLY.result() == 2188189693529


if __name__ == '__main__':
    raw = open(f'{cd}/input.txt').read()
    poly = Polymer.parse(raw)
    poly.step(10)
    print(poly.result())
