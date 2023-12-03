"""
--- Day 3: Spiral Memory ---
You come across an experimental new kind of memory stored on an infinite two-dimensional grid.

Each square on the grid is allocated in a spiral pattern starting at a location marked 1 and then
 counting up while spiraling outward. For example, the first few squares are allocated like this:

17  16  15  14  13
18   5   4   3  12
19   6   1   2  11
20   7   8   9  10
21  22  23---> ...
While this is very space-efficient (no squares are skipped), requested data must be carried 
back to square 1 (the location of the only access port for this memory system) by programs 
that can only move up, down, left, or right. They always take the shortest path: the Manhattan Distance 
between the location of the data and square 1.

For example:

Data from square 1 is carried 0 steps, since it's at the access port.
Data from square 12 is carried 3 steps, such as: down, left, left.
Data from square 23 is carried only 2 steps: up twice.
Data from square 1024 must be carried 31 steps.
How many steps are required to carry the data from the square identified 
in your puzzle input all the way to the access port?

Your puzzle input is 368078. -> 371

--- Part Two ---
As a stress test on the system, the programs here clear the grid and then store the value 1 in square 1. Then, in the same allocation order as shown above, they store the sum of the values in all adjacent squares, including diagonals.

So, the first few squares' values are chosen as follows:

Square 1 starts with the value 1.
Square 2 has only one adjacent filled square (with value 1), so it also stores 1.
Square 3 has both of the above squares as neighbors and stores the sum of their values, 2.
Square 4 has all three of the aforementioned squares as neighbors and stores the sum of their values, 4.
Square 5 only has the first and fourth squares as neighbors, so it gets the value 5.
Once a square is written, its value does not change. Therefore, the first few squares would receive the following values:

147  142  133  122   59
304    5    4    2   57
330   10    1    1   54
351   11   23   25   26
362  747  806--->   ...
What is the first value written that is larger than your puzzle input? -> 369601
"""
from collections import defaultdict
import math
from typing import Tuple, Dict, Iterator
import itertools

def find_odd_squareroot(x: int) -> int:
    """
    Find the odd number n such that
    n ** 2 <= x <= (n+2) ** 2
    """
    # largest integer m with m**2 <= x
    sqrt_x = int(math.sqrt(x))
    if sqrt_x % 2 == 0:
        return sqrt_x - 1
    else:
        return sqrt_x

assert find_odd_squareroot(25) == 5
assert find_odd_squareroot(24) == 3
assert find_odd_squareroot(26) == 5
assert find_odd_squareroot(1) == 1
    
def find_coordinates(num: int)-> Tuple[int, int]:
    sqrt = find_odd_squareroot(num)
    x = y = sqrt // 2
    
    square = sqrt ** 2
   
    if num == square:
        return (x,y)

    side_length = sqrt + 1
    # right side
    if num <= square + side_length:
        excess = num - square
        return (x + 1, y + 1 - excess)
    # top side
    elif num <= square + 2 * side_length:
        excess = num - square - side_length
        return (x + 1 - excess, y + 1 - side_length)
    # left side
    elif num <= square + 3 * side_length:
        excess = num - square - 2 * side_length
        return (-x - 1 , -y - 1 + excess)
    # bottom side
    else:
        excess = num - square - 3 * side_length
        return (-x - 1 + excess, y + 1)


assert find_coordinates(1) == (0, 0)
assert find_coordinates(9) == (1, 1)
assert find_coordinates(25) == (2, 2)
assert find_coordinates(26) == (3, 2)
assert find_coordinates(27) == (3, 1)
assert find_coordinates(31) == (3, -3)
assert find_coordinates(32) == (2, -3)
assert find_coordinates(33) == (1, -3)
assert find_coordinates(37) == (-3, -3)
assert find_coordinates(38) == (-3, -2)
assert find_coordinates(39) == (-3, -1)
assert find_coordinates(43) == (-3, 3)
assert find_coordinates(44) == (-2, 3)
assert find_coordinates(48) == (2, 3)
assert find_coordinates(49) == (3, 3)

def distance_to_center(num: int) -> int:
    x, y = find_coordinates(num)

    return abs(x) + abs(y)

assert distance_to_center(1) == 0
assert distance_to_center(12) == 3
assert distance_to_center(23) == 2
assert distance_to_center(1024) == 31

def get_neighbors(loc: Tuple[int, int]) -> Iterator[Tuple[int, int]]:
    x, y = loc
    yield x + 1, y
    yield x + 1, y - 1
    yield x, y - 1
    yield x - 1, y - 1
    yield x - 1, y
    yield x - 1, y + 1
    yield x, y + 1
    yield x + 1, y + 1


def first_value_larger_than(num: int) -> int:
    grid: Dict[Tuple[int,int], int] = defaultdict(int)

    grid[(0,0)] = 1

    for i in itertools.count(2):
        loc = find_coordinates(i)

        value = sum(grid[neighbor]
                    for neighbor in get_neighbors(loc))
        if value > num:
            return value
        grid[loc] = value

assert first_value_larger_than(400) == 747
assert first_value_larger_than(747) == 806

if __name__ == '__main__':
    print(distance_to_center(368078))
    print(first_value_larger_than(368078))