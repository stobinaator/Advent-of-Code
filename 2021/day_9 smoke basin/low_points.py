"""
--- Day 9: Smoke Basin ---
These caves seem to be lava tubes. Parts are even still volcanically active; small hydrothermal vents release smoke into the caves that slowly settles like rain.

If you can model how the smoke flows through the caves, you might be able to avoid it and be that much safer. The submarine generates a heightmap of the floor of the nearby caves for you (your puzzle input).

Smoke flows to the lowest point of the area it's in. For example, consider the following heightmap:

2199943210
3987894921
9856789892
8767896789
9899965678
Each number corresponds to the height of a particular location, where 9 is the highest and 0 is the lowest a location can be.

Your first goal is to find the low points - the locations that are lower than any of its adjacent locations. Most locations have four adjacent locations (up, down, left, and right); locations on the edge or corner of the map have three or two adjacent locations, respectively. (Diagonal locations do not count as adjacent.)

In the above example, there are four low points, all highlighted: two are in the first row (a 1 and a 0), one is in the third row (a 5), and one is in the bottom row (also a 5). All other locations on the heightmap have some lower adjacent location, and so are not low points.

The risk level of a low point is 1 plus its height. In the above example, the risk levels of the low points are 2, 1, 6, and 6. The sum of the risk levels of all low points in the heightmap is therefore 15.

Find all of the low points on your heightmap. What is the sum of the risk levels of all low points on your heightmap?

Your puzzle answer was 465.


--- Part Two ---
Next, you need to find the largest basins so you know what areas are most important to avoid.

A basin is all locations that eventually flow downward to a single low point. Therefore, every low point has a basin, although some basins are very small. Locations of height 9 do not count as being in any basin, and all other locations will always be part of exactly one basin.

The size of a basin is the number of locations within the basin, including the low point. The example above has four basins.

The top-left basin, size 3:

2199943210
3987894921
9856789892
8767896789
9899965678
The top-right basin, size 9:

2199943210
3987894921
9856789892
8767896789
9899965678
The middle basin, size 14:

2199943210
3987894921
9856789892
8767896789
9899965678
The bottom-right basin, size 9:

2199943210
3987894921
9856789892
8767896789
9899965678
Find the three largest basins and multiply their sizes together. In the above example, this is 9 * 14 * 9 = 1134.

What do you get if you multiply together the sizes of the three largest basins?
1269555
"""

from typing import List, Tuple
import os

cd = os.path.abspath(os.getcwd())

RAW = """2199943210
3987894921
9856789892
8767896789
9899965678"""

INPUT = [[int(nr.strip()) for nr in row] for row in RAW.split()]


class HeightMap:
    def __init__(self, map: List[List[int]]) -> None:
        self.map = map
        self.nr = len(map)
        self.nc = len(map[0])
        self.low_points = []
        self.nrs_in_diff_directions = []
        self.min_number = 0

    def iterate_map(self) -> None:
        for i in range(self.nr):
            for j in range(self.nc):
                self.nrs_in_diff_directions.clear()
                self.min_number = 0

                # top left diagonal
                if i == 0 and j == 0:
                    if (self.map[i][j] < self.map[i][j + 1]) and (
                        self.map[i][j] < self.map[i + 1][j]
                    ):
                        self.low_points.append(self.map[i][j])

                # top right diagonal
                elif i == 0 and j == self.nc - 1:
                    if (self.map[i][j] < self.map[i][j - 1]) and (
                        self.map[i][j] < self.map[i + 1][j]
                    ):
                        self.low_points.append(self.map[i][j])

                # bottom left diagonal
                elif i == self.nr - 1 and j == 0:
                    if (self.map[i][j] < self.map[i - 1][j]) and (
                        self.map[i][j] < self.map[i][j + 1]
                    ):
                        self.low_points.append(self.map[i][j])

                # bottom right diagonal
                elif i == self.nr - 1 and j == self.nc - 1:
                    if (self.map[i][j] < self.map[i - 1][j]) and (
                        self.map[i][j] < self.map[i][j - 1]
                    ):
                        self.low_points.append(self.map[i][j])

                # square- minus top/bottom row & minus far-left/far-right column
                elif (1 <= i <= self.nr - 2) and (1 <= j <= self.nc - 2):
                    self.nrs_in_four_dirs((i, j))

                # whole first/last row
                elif i in [0, self.nr - 1] and (1 <= j <= self.nc - 2):
                    self.nrs_in_three_dirs_horiz((i, j))

                # whole far-left/right col
                elif (1 <= i <= self.nr - 2) and j in [0, self.nc - 1]:
                    self.nrs_in_three_dirs_vert((i, j))

    def nrs_in_four_dirs(self, coords: Tuple[int, int]) -> None:
        i, j = coords
        curr_nr = self.map[i][j]
        self.nrs_in_diff_directions.append(self.map[i][j + 1])  # nr to the right
        self.nrs_in_diff_directions.append(self.map[i][j - 1])  # nr to the left
        self.nrs_in_diff_directions.append(self.map[i + 1][j])  # nr to the top
        self.nrs_in_diff_directions.append(self.map[i - 1][j])  # nr to the botton
        self.min_number = min(self.nrs_in_diff_directions)
        if curr_nr < self.min_number:
            self.low_points.append(self.map[i][j])

    def nrs_in_three_dirs_horiz(self, coords: Tuple[int, int]) -> None:
        i, j = coords
        curr_nr = self.map[i][j]
        if i == 0:
            self.nrs_in_diff_directions.append(self.map[i][j - 1])  # nr to left
            self.nrs_in_diff_directions.append(self.map[i][j + 1])  # nr to right
            self.nrs_in_diff_directions.append(self.map[i + 1][j])  # nr to bottom
        elif i == self.nr - 1:
            self.nrs_in_diff_directions.append(self.map[i][j - 1])  # nr to left
            self.nrs_in_diff_directions.append(self.map[i][j + 1])  # nr to right
            self.nrs_in_diff_directions.append(self.map[i - 1][j])  # nr to top
        self.min_number = min(self.nrs_in_diff_directions)
        if curr_nr < self.min_number:
            self.low_points.append(self.map[i][j])

    def nrs_in_three_dirs_vert(self, coords: Tuple[int, int]) -> None:
        i, j = coords
        curr_nr = self.map[i][j]
        if j == 0:
            self.nrs_in_diff_directions.append(self.map[i - 1][j])  # nr to top
            self.nrs_in_diff_directions.append(self.map[i][j + 1])  # nr to right
            self.nrs_in_diff_directions.append(self.map[i + 1][j])  # nr to bottom
        elif j == self.nc - 1:
            self.nrs_in_diff_directions.append(self.map[i - 1][j])  # nr to top
            self.nrs_in_diff_directions.append(self.map[i][j - 1])  # nr to right
            self.nrs_in_diff_directions.append(self.map[i + 1][j])  # nr to bottom
        self.min_number = min(self.nrs_in_diff_directions)
        if curr_nr < self.min_number:
            self.low_points.append(self.map[i][j])

    def calc_risk_level(self) -> int:
        return sum(x + 1 for x in self.low_points)

    @staticmethod
    def parse(map: str) -> "HeightMap":
        numbers_map = [[int(nr.strip()) for nr in row] for row in map.split()]
        return HeightMap(numbers_map)


HM = HeightMap.parse(RAW)
HM.iterate_map()
print(HM.calc_risk_level())

if __name__ == "__main__":
    input = open(f"{cd}/input.txt").read()
    hm = HeightMap.parse(input)
    hm.iterate_map()
    print(hm.calc_risk_level())
