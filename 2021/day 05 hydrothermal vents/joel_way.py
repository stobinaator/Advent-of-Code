import os
from dataclasses import dataclass
from typing import NamedTuple, Iterator, Iterable
from collections import Counter

RAW = """0,9 -> 5,9
8,0 -> 0,8
9,4 -> 3,4
2,2 -> 2,1
7,0 -> 7,4
6,4 -> 2,0
0,9 -> 2,9
3,4 -> 1,4
0,0 -> 8,8
5,5 -> 8,2"""

class Point(NamedTuple):
    x: int
    y: int

    @staticmethod
    def parse(raw: str) -> 'Point':
        x, y = raw.split(',')
        print(x,y)
        return Point(int(x),int(y))

@dataclass
class Line(NamedTuple):
    start: Point
    end: Point

    def is_horizontal(self) -> bool:
        return self.start.y == self.end.y

    def is_vertical(self) -> bool:
        return self.start.x == self.end.x

    def points_on_line(self) -> Iterator[Point]:
        if self.is_horizontal():
            lo = min(self.start.x, self.end.x)
            hi = max(self.start.x, self.end.x)

            for x in range(lo, hi+1):
                yield Point(x, self.start.y)
        elif self.is_vertical():
            lo = min(self.start.y, self.end.y)
            hi = max(self.start.y, self.end.y)

            for y in range(lo, hi+1):
                yield Point(self.start.x, y)
        else:
            # the line is 45 degrees
            x_lo = min(self.start.x, self.end.x)
            x_hi = max(self.start.x, self.end.x)

            dx = self.end.x - self.start.x
            dy = self.end.y - self.start.y
            slopes_up = dx * dy > 0

            for i in range(x_hi - x_lo + 1):
                x = x_lo + i
                y = self.start.y + i * (1 if slopes_up else -1)
                
                yield Point(x,y)
                

    @staticmethod
    def parse(raw: str) -> 'Line':
        start_raw, end_raw = raw.split(' -> ')
        return Line(Point.parse(start_raw), Point.parse(end_raw))

def count_vents(lines: Iterable[Line], hv_only=True) -> int:
    counts = Counter(
        point
        for line in lines
        if any([not hv_only, line.is_horizontal(), line.is_vertical()])
        for point in line.points_on_line()
    )

    return sum(count >= 2 for count in counts.values())

LINES = [Line.parse(raw) for raw in RAW.splitlines()]
assert count_vents(LINES) == 5
assert count_vents(LINES, hv_only=False) == 12
"""
if __name__ == '__main__':
    cd = os.path.abspath(os.getcwd())
    raw = open(f'{cd}/input.txt').read()
    lines = [Line.parse(raw) for raw in raw.splitlines()]
    print(count_vents(lines))"""