"""
--- Day 13: Transparent Origami ---
You reach another volcanically active part of the cave. It would be nice if you could do some kind of thermal imaging so you could tell ahead of time which caves are too hot to safely enter.

Fortunately, the submarine seems to be equipped with a thermal camera! When you activate it, you are greeted with:

Congratulations on your purchase! To activate this infrared thermal imaging
camera system, please enter the code found on page 1 of the manual.
Apparently, the Elves have never used this feature. To your surprise, you manage to find the manual; as you go to open it, page 1 falls out. It's a large sheet of transparent paper! The transparent paper is marked with random dots and includes instructions on how to fold it up (your puzzle input). For example:

The first section is a list of dots on the transparent paper. 0,0 represents the top-left coordinate. The first value, x, increases to the right. The second value, y, increases downward. So, the coordinate 3,0 is to the right of 0,0, and the coordinate 0,7 is below 0,0. The coordinates in this example form the following pattern, where # is a dot on the paper and . is an empty, unmarked position:

Then, there is a list of fold instructions. Each instruction indicates a line on the transparent paper and wants you to fold the paper up (for horizontal y=... lines) or left (for vertical x=... lines). In this example, the first fold instruction is fold along y=7, which designates the line formed by all of the positions where y is 7 (marked here with -):

Now, only 17 dots are visible.

Notice, for example, the two dots in the bottom left corner before the transparent paper is folded; after the fold is complete, those dots appear in the top left corner (at 0,0 and 0,1). Because the paper is transparent, the dot just below them in the result (at 0,3) remains visible, as it can be seen through the transparent paper.

Also notice that some dots can end up overlapping; in this case, the dots merge together and become a single dot.

The second fold instruction is fold along x=5, which indicates this line:

Because this is a vertical line, fold left:

The instructions made a square!

The transparent paper is pretty big, so for now, focus on just completing the first fold. After the first fold in the example above, 17 dots are visible - dots that end up overlapping after the fold is completed count as a single dot.

How many dots are visible after completing just the first fold instruction on your transparent paper?
814

--- Part Two ---
Finish folding the transparent paper according to the instructions. The manual says the code is always eight capital letters.

What code do you use to activate the infrared thermal imaging camera system?

"""
from collections import defaultdict
from typing import List


RAW = """6,10
0,14
9,10
0,3
10,4
4,11
6,0
6,12
4,1
0,13
10,12
3,4
3,0
8,4
1,10
2,14
8,10
9,0

fold along y=7
fold along x=5"""


class Origami:
    def __init__(self, points: List[List[int]], folding: List[str]) -> None:
        self.points = sorted(points)
        self.folding = folding
        self.maxr = max(x[1] for x in self.points)
        self.maxc = max(x[0] for x in self.points)
        self.recognized = [ [False
                            for _ in range(self.maxc+1)]
                            for _ in range(self.maxr+1)]


    def place_points(self) -> None:
        for pnt in self.points:
            x,y = pnt[0], pnt[1]
            for i in range(self.maxc+1):
                if i == x:
                    for j in range(self.maxr+1):
                        if j == y:
                            self.recognized[j][i] = True
                    
    def fold(self):
        """
        FOLD UP
        if an x is given to be folded on
        the bottom part is being folded upwards
        6,10 slice y=7 
        -> y_now = 10, (y_now - slice) * 2 = (10 - 7) * 2 = 6 (distance)
        -> y_new = 10 - distance (6) = 4

        FOLD LEFT
        if an y is given to be folded on
        the right part is being folded to the left
        6,0 slice x=5
        -> x_now = 6, (x_now - slice) * 2 = (6-5) * 2 = 2 (distance)
        -> x_new = x_now (6) - distance (2) = 4
        """
        if self.folding[0].startswith('y'):
            fold_row = int(self.folding[0].split('=')[-1])
            for i in range(fold_row+1, self.maxr+1):
                for j in range(self.maxc+1):
                    if self.recognized[i][j] == True:
                        y_dist = (i - fold_row) * 2
                        i_new =  abs(i - y_dist)
                        self.recognized[i_new][j] = True
            del self.folding[0]
            self.recognized = self.recognized[:fold_row]

        elif self.folding[0].startswith('x'):
            fold_row = int(self.folding[0].split('=')[-1])
            for i in range(fold_row):
                for j in range(self.maxc+1):
                    if self.recognized[i][j] == True:
                        i_dist = (j - fold_row) * 2
                        j_new =  abs(j - i_dist)
                        self.recognized[i][j_new] = True
            del self.folding[0]
            self.recognized = [lst[:fold_row] for lst in self.recognized]
            

    def count_points(self) -> int:
        return sum(sum(x) for x in self.recognized)

    @staticmethod
    def parse(points: str) -> 'Origami':
        r_inpt = [line.strip() for line in points.splitlines() if line != '']
        folding = [p[11:] for p in r_inpt[-2:]]
        r_inpt = [[int(t) for t in tup.split(',')] for tup in r_inpt[:-2]]
        
        return Origami(r_inpt, folding)

    @staticmethod
    def parse2(points: str) -> 'Origami':
        r_inpt = [line.strip() for line in points.splitlines() if line != '']
        folding = [p[11:] for p in r_inpt[-12:]]
        r_inpt = [[int(t) for t in tup.split(',')] for tup in r_inpt[:-12]]
        
        return Origami(r_inpt, folding)

org = Origami.parse(RAW)
org.place_points()
org.fold()
print(org.count_points())
org.fold()
print(org.count_points())

