from typing import Iterable, Iterator, Tuple
import os

cd = os.path.abspath(os.getcwd())

RAW = """2199943210
3987894921
9856789892
8767896789
9899965678"""

class HeightMap:
    def __init__(self, raw: str):
        self.map = [[int(val) for val in row] for row in raw.splitlines()]
        self.nr = len(self.map)
        self.nc = len(self.map[0])

    def neighbors(self, r: int, c: int) -> Iterator[Tuple[int, int]]:
        for dr, dc in ((-1,0), (1, 0), (0, -1), (0, 1)):
            if 0 <= r + dr < self.nr and 0 <= c + dc < self.nc:
                yield r+dr, c+dc
    
    def is_low_point(self, r: int, c: int) -> bool:
        return all(
            self.map[r][c] < self.map[r_][c_]
            for r_, c_ in self.neighbors(r, c)
        )
    
    def risk_level(self, r: int, c: int) -> int:
        return self.map[r][c] + 1

    def total_risk_level_of_low_points(self) -> int:
        return sum(
            self.risk_level(r, c)
            for r in range(self.nr)
            for c in range(self.nc)
            if self.is_low_point(r, c)
        )
    
HM = HeightMap(RAW)   
assert HM.total_risk_level_of_low_points() == 15

if __name__ == '__main__':
    raw = open(f'{cd}/input.txt').read()
    hm = HeightMap(raw)
    print(hm.total_risk_level_of_low_points())