"""
--- Day 11: Dumbo Octopus ---
You enter a large cavern full of rare bioluminescent dumbo octopuses! They seem to not like the Christmas lights on your submarine, so you turn them off for now.

There are 100 octopuses arranged neatly in a 10 by 10 grid. Each octopus slowly gains energy over time and flashes brightly for a moment when its energy is full. Although your lights are off, maybe you could navigate through the cave without disturbing the octopuses if you could predict when the flashes of light will happen.

Each octopus has an energy level - your submarine can remotely measure the energy level of each octopus (your puzzle input). For example:

5483143223
2745854711
5264556173
6141336146
6357385478
4167524645
2176841721
6882881134
4846848554
5283751526
The energy level of each octopus is a value between 0 and 9. Here, the top-left octopus has an energy level of 5, the bottom-right one has an energy level of 6, and so on.

You can model the energy levels and flashes of light in steps. During a single step, the following occurs:

First, the energy level of each octopus increases by 1.
Then, any octopus with an energy level greater than 9 flashes. This increases the energy level of all adjacent octopuses by 1, including octopuses that are diagonally adjacent. If this causes an octopus to have an energy level greater than 9, it also flashes. This process continues as long as new octopuses keep having their energy level increased beyond 9. (An octopus can only flash at most once per step.)
Finally, any octopus that flashed during this step has its energy level set to 0, as it used all of its energy to flash.
Adjacent flashes can cause an octopus to flash on a step even if it begins that step with very little energy. Consider the middle octopus with 1 energy in this situation:

Before any steps:
11111
19991
19191
19991
11111

After step 1:
34543
40004
50005
40004
34543

After step 2:
45654
51115
61116
51115
45654

Before any steps:
5483143223
2745854711
5264556173
6141336146
6357385478
4167524645
2176841721
6882881134
4846848554
5283751526

After step 1:
6594254334
3856965822
6375667284
7252447257
7468496589
5278635756
3287952832
7993992245
5957959665
6394862637

After step 2:
8807476555
5089087054
8597889608
8485769600
8700908800
6600088989
6800005943
0000007456
9000000876
8700006848

An octopus is highlighted when it flashed during the given step.
After step 10, there have been a total of 204 flashes
After 100 steps, there have been a total of 1656 flashes.

Given the starting energy levels of the dumbo octopuses in your cavern, simulate 100 steps. How many total flashes are there after 100 steps?
1620

--- Part Two ---
It seems like the individual flashes aren't bright enough to navigate. However, you might have a better option: the flashes seem to be synchronizing!

In the example above, the first time all octopuses flash simultaneously is step 195:

If you can calculate the exact moments when the octopuses will all flash simultaneously, you should be able to navigate through the cavern. What is the first step during which all octopuses flash?
"""
from io import IncrementalNewlineDecoder
from typing import List, Tuple
import os

cd = os.path.abspath(os.getcwd())

REAL_INPUT = """7147713556
6167733555
5183482118
3885424521
7533644611
3877764863
7636874333
8687188533
7467115265
1626573134"""

RAW = """11111
19991
19191
19991
11111"""

RAW2 = """5483143223
2745854711
5264556173
6141336146
6357385478
4167524645
2176841721
6882881134
4846848554
5283751526"""

class OctoCavern:
    def __init__(self, dumbo_octopuses: List[List[int]]) -> None:
        self.octopuses = dumbo_octopuses
        self.recognized = [[False for x in board_row]
                            for board_row in self.octopuses]
        self.nr = len(self.octopuses)
        self.nc = len(self.octopuses[0])

    def step(self) -> None:
        """
        increments each octopus' counter
        """
        for i in range(self.nr):
            for j in range(self.nc):
                self.octopuses[i][j] += 1

    def check_for_Xs(self) -> None:
        for i in range(self.nr):
            for j in range(self.nc):
                if self.octopuses[i][j] == 10:
                    self.increment_neighbors((i,j))
                    #self.check_if_new_Xs()
        self.clean_tens()
    """
    def check_if_new_Xs(self) -> None:
        for x in range(self.nr):
            for y in range(self.nc):
                if self.recognized[x][y] == True:
                    self.incr_for_one_cells_neighs((x,y))

    def incr_for_one_cells_neighs(self, loc: Tuple[int, int]) -> None:
        x,y = loc
        for hor, vert in ((x+1,y),(x+1,y+1),(x,y+1),(x-1,y+1),(x-1,y),(x-1,y-1),(x,y-1),(x+1,y-1)): 
            if 0 <= hor < self.nr and 0 <= vert < self.nc:
                    self.octopuses[hor][vert] += 1
        self.recognized[x][y] = False
    """
    def increment_neighbors(self, loc: Tuple[int, int]) -> None:
        x,y = loc
        for hor, vert in ((x+1,y),(x+1,y+1),(x,y+1),(x-1,y+1),(x-1,y),(x-1,y-1),(x,y-1),(x+1,y-1)): 
            if 0 <= hor < self.nr and 0 <= vert < self.nc:
                if self.octopuses[hor][vert] != 10:
                    if self.octopuses[hor][vert] + 1 == 10:
                        self.octopuses[hor][vert] += 1
                        self.recognized[hor][vert] = True
                    else:
                        self.octopuses[hor][vert] += 1
                
                """
                if self.octopuses[hor][vert] == 10:
                    continue
                elif self.octopuses[hor][vert] != 10 and self.octopuses[hor][vert] + 1 > 9:
                    self.octopuses[hor][vert] += 1
                    self.recognized[hor][vert] = True
                elif self.octopuses[hor][vert] != 10:
                    self.octopuses[hor][vert] += 1 
                """
    def clean_tens(self) -> None:
        self.octopuses = [[0 if num == 10 else num for num in lst] for lst in self.octopuses]
        self.recognized = [[False for x in board_row]
                            for board_row in self.octopuses]

    def display_octopuses(self) -> None:
        for i in range(self.nc):
            print(self.octopuses[i])

    def display_recognized(self) -> None:
        for i in range(self.nc):
            print(self.recognized[i])

    @staticmethod
    def parse(dumbo_octopuses: str) -> 'OctoCavern':
        return OctoCavern([[int(nr) for nr in line] for line in dumbo_octopuses.splitlines()])

oc = OctoCavern.parse(RAW2)
for i in range(2):
    oc.step()
    oc.check_for_Xs()

oc.display_octopuses()
