from collections import namedtuple
from typing import Counter, List, Tuple
import os 

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

Point = namedtuple('Point', ['x', 'y'])


# fugly
def get_line_seg(start_pt: Point, end_pt: Point, part: int = 1) -> List[Point]:
    line_seg = []
    line_seg.append(start_pt)
    line_seg.append(end_pt)

    y_end = max([start_pt.y, end_pt.y])
    y_start = min([start_pt.y, end_pt.y])
    x_end = max([start_pt.x, end_pt.x])
    x_start = min([start_pt.x, end_pt.x])

    if start_pt.x == end_pt.x:
        y_dist = y_end - y_start

        for y in range(1, y_dist):
            line_seg.append(Point(start_pt.x, y_start+y))

    elif start_pt.y == end_pt.y:
        x_dist = x_end - x_start

        for x in range(1, x_dist):
            line_seg.append(Point(x_start + x, start_pt.y))
    else:
        if part == 1:
            line_seg = []
        else:
            direction = Point(x=1 if (end_pt.x-start_pt.x) > 0 else -1,
                              y=1 if (end_pt.y-start_pt.y) > 0 else -1)
            i = 1
            while True:
                pt = Point(start_pt.x+i*direction.x, start_pt.y+i*direction.y)
                if pt in line_seg:
                    break
                line_seg.append(pt)
                i += 1
    return line_seg


def input_to_segments(input_string: str) -> List[Tuple[int, int, int, int]]:
    seg_pts = []
    for line in input_string.splitlines():
        left, right = line.split(' -> ')
        r_x, r_y = [int(x) for x in right.split(',')]
        l_x, l_y = [int(x) for x in left.split(',')]
        seg_pts.append((l_x, l_y, r_x, r_y))
    return seg_pts


def count_intersections(input_str: str, part: int = 1) -> int:
    segments_pts = input_to_segments(input_str)
    line_segments = []
    for segment in segments_pts:
        x1, y1, x2, y2 = segment
        line_segments.extend(get_line_seg(Point(x1, y1), Point(x2, y2), part))

    pts_ctr = Counter(line_segments)
    counts = pts_ctr.values()
    return sum(1 for x in counts if x >= 2)


assert count_intersections(RAW) == 5
assert count_intersections(RAW, 2) == 12, count_intersections(RAW, 2)

if __name__ == "__main__":
    cd = os.path.abspath(os.getcwd())
    inp = open(f"{cd}/input.txt").read()
    print(count_intersections(inp))
    print(count_intersections(inp, 2))