"""
--- Day 4: Giant Squid ---
You're already almost 1.5km (almost a mile) below the surface of the ocean, already so deep that you can't see any sunlight. What you can see, however, is a giant squid that has attached itself to the outside of your submarine.

Maybe it wants to play bingo?

Bingo is played on a set of boards each consisting of a 5x5 grid of numbers. Numbers are chosen at random, and the chosen number is marked on all boards on which it appears. (Numbers may not appear on all boards.) If all numbers in any row or any column of a board are marked, that board wins. (Diagonals don't count.)

The submarine has a bingo subsystem to help passengers (currently, you and the giant squid) pass the time. It automatically generates a random order in which to draw numbers and a random set of boards (your puzzle input). For example:

7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1

22 13 17 11  0
 8  2 23  4 24
21  9 14 16  7
 6 10  3 18  5
 1 12 20 15 19

 3 15  0  2 22
 9 18 13 17  5
19  8  7 25 23
20 11 10 24  4
14 21 16 12  6

14 21 17 24  4
10 16 15  9 19
18  8 23 26 20
22 11 13  6  5
 2  0 12  3  7
After the first five numbers are drawn (7, 4, 9, 5, and 11), there are no winners, but the boards are marked as follows (shown here adjacent to each other to save space):

22 13 17 11  0         3 15  0  2 22        14 21 17 24  4
 8  2 23  4 24         9 18 13 17  5        10 16 15  9 19
21  9 14 16  7        19  8  7 25 23        18  8 23 26 20
 6 10  3 18  5        20 11 10 24  4        22 11 13  6  5
 1 12 20 15 19        14 21 16 12  6         2  0 12  3  7
After the next six numbers are drawn (17, 23, 2, 0, 14, and 21), there are still no winners:

22 13 17 11  0         3 15  0  2 22        14 21 17 24  4
 8  2 23  4 24         9 18 13 17  5        10 16 15  9 19
21  9 14 16  7        19  8  7 25 23        18  8 23 26 20
 6 10  3 18  5        20 11 10 24  4        22 11 13  6  5
 1 12 20 15 19        14 21 16 12  6         2  0 12  3  7
Finally, 24 is drawn:

22 13 17 11  0         3 15  0  2 22        14 21 17 24  4
 8  2 23  4 24         9 18 13 17  5        10 16 15  9 19
21  9 14 16  7        19  8  7 25 23        18  8 23 26 20
 6 10  3 18  5        20 11 10 24  4        22 11 13  6  5
 1 12 20 15 19        14 21 16 12  6         2  0 12  3  7
At this point, the third board wins because it has at least one complete row or column of marked numbers (in this case, the entire top row is marked: 14 21 17 24 4).

The score of the winning board can now be calculated. Start by finding the sum of all unmarked numbers on that board; in this case, the sum is 188. Then, multiply that sum by the number that was just called when the board won, 24, to get the final score, 188 * 24 = 4512.

To guarantee victory against the giant squid, figure out which board will win first. What will your final score be if you choose that board?
6592
"""

import os
import copy
from itertools import islice
from typing import List, Tuple


cd = os.path.abspath(os.getcwd())


def to_list(path_to_txt) -> Tuple[List[List[List[int]]], List[int]]:
    bingo_splt = list()
    with open(path_to_txt, "r") as f:
        content = f.read()
        # holds all the lines
        content_list = content.splitlines()

        # this is the 1st row
        draw_nrs = [int(num) for num in content_list[0].split(",")]

        # List[str]
        bingo_rows = [thing for thing in content_list[1:] if thing != ""]

        # List[List[str]]
        bingo_rows_split = [b.strip().replace(" ", ",").split(",") for b in bingo_rows]

        # List[List[int]]
        for elem in bingo_rows_split:
            bingo_splt.append([int(x) for x in elem if x != ""])

        last_list = list()
        for i in range(len(bingo_splt) // 5):
            last_list.append(bingo_splt[i * 5 : 5 * (i + 1)])

    return last_list, draw_nrs


def count_rest_sum(bingo_board: List[int], drawn_number: int) -> int:
    count = 0
    for i in range(5):
        for j in range(5):
            if isinstance(bingo_board[i][j], int):
                count += bingo_board[i][j]
    return count * drawn_number


def check_if_winner(bingo_board: List[int], drawn_number: int):
    counter_cols = []
    counter_rows = [list(map(lambda x: x == "X", row)) for row in bingo_board]

    for i in range(5):
        col = [x[i] for x in bingo_board]
        counter_cols.append(list(map(lambda x: x == "X", col)))

    row_counts = [sum(ro) for ro in counter_rows]
    col_counts = [sum(co) for co in counter_cols]

    row_res = [num == 5 for num in row_counts]
    col_res = [num == 5 for num in col_counts]

    for x in row_res + col_res:
        if x:
            return count_rest_sum(bingo_board, drawn_number)
    return False


def solve_it(bingo_array: List[List[int]], draw_nrs: List[int]) -> int:
    bingo_copy = copy.deepcopy(bingo_array)
    for number in draw_nrs:
        for x in range(len(bingo_array)):
            for i in range(5):
                for j in range(5):
                    if bingo_array[x][i][j] == number:
                        bingo_copy[x][i][j] = "X"
                        count = check_if_winner(bingo_copy[x], number)
                        if count:
                            return count


def part_one() -> int:
    PATH = f"{cd}/input.txt"
    bingo_board, draw_nrs = to_list(PATH)
    return solve_it(bingo_board, draw_nrs)


# print(part_one())
"""
--- Part Two ---
On the other hand, it might be wise to try a different strategy: let the giant squid win.

You aren't sure how many bingo boards a giant squid could play at once, so rather than waste time counting its arms, the safe thing to do is to figure out which board will win last and choose that one. That way, no matter which boards it picks, it will win for sure.

In the above example, the second board is the last to win, which happens after 13 is eventually called and its middle column is completely marked. If you were to keep playing until this point, the second board would have a sum of unmarked numbers equal to 148 for a final score of 148 * 13 = 1924.

Figure out which board will win last. Once it wins, what would its final score be?
31755
"""

example_array = [
    [
        [14, 21, 17, 24, 4],
        [10, 16, 15, 9, 19],
        [18, 8, 23, 26, 20],
        [22, 11, 13, 6, 5],
        [2, 0, 12, 3, 7],
    ],
    [
        [3, 15, 0, 2, 22],
        [9, 18, 13, 17, 5],
        [19, 8, 7, 25, 23],
        [14, 21, 16, 12, 6],
        [20, 11, 10, 24, 4],
    ],
    [
        [22, 13, 17, 11, 0],
        [8, 2, 23, 4, 24],
        [21, 9, 14, 16, 7],
        [6, 10, 3, 18, 5],
        [1, 12, 20, 15, 19],
    ],
]

PATH = f"{cd}/ex_input.txt"
bingo_board, draw_nrs = to_list(PATH)
# print(solve_it(bingo_board, draw_nrs))


def solve_it2(bingo_array: List[List[int]], draw_nrs: List[int]) -> int:
    bingo_copy = copy.deepcopy(bingo_array)
    another_copy = copy.deepcopy(bingo_array)
    for number in draw_nrs:
        for x in range(len(bingo_array)):
            for i in range(5):
                for j in range(5):
                    if bingo_array[x][i][j] == number:
                        bingo_copy[x][i][j] = "X"
                        count = check_if_winner(bingo_copy[x], number)

                        if count != False:
                            print(bingo_copy)
                            del another_copy[x]
                            print(another_copy)
                            return count
                    print()


print(solve_it2(bingo_board, draw_nrs))
