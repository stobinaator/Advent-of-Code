from dataclasses import dataclass

RAW = """1000
2000
3000

4000

5000
6000

7000
8000
9000

10000"""

@dataclass
class Elf:
    foods: list[int]

    def cals(self) -> int:
        return sum(self.foods)

def parse(raw: str) -> list[Elf]:
    return [
        Elf([int(x) for x in line.split("\n")])
        for line in raw.strip().split("\n\n")
    ]

with open("input.txt") as f:
    elves = parse(f.read())

print(max(elf.cals() for elf in elves))

print(sum(elf.cals() for elf in sorted(elves, key=lambda elf: elf.cals(), reverse=True)[:3]))