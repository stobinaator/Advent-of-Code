"""
--- Day 1: Sonar Sweep ---
You're minding your own business on a ship at sea when the overboard alarm goes off! 
You rush to see if you can help. Apparently, one of the Elves tripped and accidentally sent the 
sleigh keys flying into the ocean!

Before you know it, you're inside a submarine the Elves keep ready for situations like this. 
It's covered in Christmas lights (because of course it is), and it even has an experimental antenna 
that should be able to track the keys if you can boost its signal strength high enough; there's a 
little meter that indicates the antenna's signal strength by displaying 0-50 stars.

Your instincts tell you that in order to save Christmas, you'll need to get all fifty stars by December 25th.

Collect stars by solving puzzles. Two puzzles will be made available on each day in the Advent calendar; 
the second puzzle is unlocked when you complete the first. Each puzzle grants one star. Good luck!

As the submarine drops below the surface of the ocean, it automatically performs a sonar sweep of the 
nearby sea floor. On a small screen, the sonar sweep report (your puzzle input) appears: each line is 
a measurement of the sea floor depth as the sweep looks further and further away from the submarine.

For example, suppose you had the following report:

199
200
208
210
200
207
240
269
260
263
This report indicates that, scanning outward from the submarine, the sonar sweep found depths of 
199, 200, 208, 210, and so on.

The first order of business is to figure out how quickly the depth increases, just so you know what 
you're dealing with - you never know if the keys will get carried into deeper water by an ocean 
current or a fish or something.

To do this, count the number of times a depth measurement increases from the previous measurement. 
(There is no measurement before the first measurement.) In the example above, the changes are as follows:
"""

import os
from typing import List
from itertools import cycle

cd = os.path.abspath(os.getcwd())

def to_ints():
    with open(f"{cd}/input.txt","r") as f:
        input_numbers = [int(number.strip()) for number in f]
    return input_numbers

def depth_increases_count(numbers_int: List[int]) -> int:
    increases = 0
    for curr_depth, next_depth in zip(numbers_int, numbers_int[1:]):
        if curr_depth < next_depth:
            increases += 1
    return increases

def depth_increases_count2(numbers_int: List[int]) -> int:
    return sum([(n2-n1)>0 for n1, n2 in zip(numbers_int, numbers_int[1:])])

def depth_increases_count3(numbers_int: List[int]) -> int:
    l1 = iter(numbers_int)
    l2 = iter(numbers_int[1:])
    while True:
        yield next(l2), next(l1)


result = to_ints()
res = depth_increases_count3(result)
print(res)

"""
--- Part Two ---
Considering every single measurement isn't as useful as you expected: there's just too much noise in the data.

Instead, consider sums of a three-measurement sliding window. Again considering the above example:

199  A      
200  A B    
208  A B C  
210    B C D
200  E   C D
207  E F   D
240  E F G  
269    F G H
260      G H
263        H
Start by comparing the first and second three-measurement windows. 
The measurements in the first window are marked A (199, 200, 208); their sum is 199 + 200 + 208 = 607. 
The second window is marked B (200, 208, 210); its sum is 618. 
The sum of measurements in the second window is larger than the sum of the first, 
so this first comparison increased.

Your goal now is to count the number of times the sum of measurements in this sliding window 
increases from the previous sum. So, compare A with B, then compare B with C, then C with D, and so on. 
Stop when there aren't enough measurements left to create a new three-measurement sum.
"""

def three_measurement_windows(nums_int: List[int]) -> int:
    increases = 0
    first_sum = 0
    second_sum = 0
    for num1, num2, num3, num4 in zip(nums_int, nums_int[1:], nums_int[2:], nums_int[3:]):
        first_sum = num1 + num2 + num3
        second_sum = num2 + num3 + num4 
        if first_sum < second_sum:
            increases += 1
    return increases

        

result = to_ints()
res = three_measurement_windows(result)
print(res)