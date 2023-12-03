'''
--- Day 2: Corruption Checksum ---
As you walk through the door, a glowing humanoid shape yells in your direction. 
"You there! Your state appears to be idle. Come help us repair the corruption in this spreadsheet - 
if we take another millisecond, we'll have to display an hourglass cursor!"

The spreadsheet consists of rows of apparently-random numbers. To make sure the recovery process 
is on the right track, they need you to calculate the spreadsheet's checksum. 
For each row, determine the difference between the largest value and the smallest value; 
the checksum is the sum of all of these differences.

For example, given the following spreadsheet:

5 1 9 5
7 5 3
2 4 6 8
The first row's largest and smallest values are 9 and 1, and their difference is 8.
The second row's largest and smallest values are 7 and 3, and their difference is 4.
The third row's difference is 6.
In this example, the spreadsheet's checksum would be 8 + 4 + 6 = 18.

What is the checksum for the spreadsheet in your puzzle input?

48357
'''
import os, sys, timeit
from typing import List
cd = os.path.abspath(os.getcwd())

def read_sequence() -> List[str]:
    with open(f"{cd}/input.txt", "r") as f:
        data = f.readlines()
        data = [item.replace('\t', ' ').replace('\n', '') for item in data] 
    return data

def read_seq2() -> List[List[int]]:
    number_list = list()
    with open(f"{cd}/input.txt", "r") as f:
        data = f.readlines()
        data = [item.replace('\t', ' ').replace('\n', '') for item in data]
        for line in data:
                split_line = line.split(' ')
                number_list.append(list(map(int, split_line)))
    return number_list

def compute_checksums_p1(data_list: List[str]) -> int:
    checksum = 0
    for line in data_list:
        split_line = line.split(' ')
        number_list = list(map(int, split_line))
        checksum += (max(number_list) - min(number_list))
    return checksum

def compute_checksums2_p1(data_list: List[List[int]]) -> int:
    checksum:int = 0
    for num_list in data_list:
        checksum += (max(num_list) - min(num_list))
    return checksum


assert compute_checksums_p1(["5 1 9 5"]) == 8
assert compute_checksums_p1(["7 5 3"]) == 4
assert compute_checksums_p1(["2 4 6 8"]) == 6
assert compute_checksums_p1(["5 1 9 5", "7 5 3", "2 4 6 8"]) == 18


input_text = read_sequence()
input_text2 = read_seq2()
result = compute_checksums_p1(read_sequence())
result2 = compute_checksums2_p1(read_seq2())
print(result, result2)

'''
--- Part Two ---
"Great work; looks like we're on the right track after all. Here's a star for your effort." 
However, the program seems a little worried. Can programs be worried?

"Based on what we're seeing, it looks like all the User wanted is some information about the evenly 
divisible values in the spreadsheet. Unfortunately, none of us are equipped for that kind of calculation 
- most of us specialize in bitwise operations."

It sounds like the goal is to find the only two numbers in each row where one evenly divides the other 
- that is, where the result of the division operation is a whole number. 
They would like you to find those numbers on each line, divide them, and add up each line's result.

For example, given the following spreadsheet:

5 9 2 8
9 4 7 3
3 8 6 5
In the first row, the only two numbers that evenly divide are 8 and 2; the result of this division is 4.
In the second row, the two numbers are 9 and 3; the result is 3.
In the third row, the result is 2.
In this example, the sum of the results would be 4 + 3 + 2 = 9.

What is the sum of each row's result in your puzzle input?
351
'''

def compute_checksums_p2(numbers: list) -> int:
    sum = 0
    for line in numbers:
        line = line.split(' ')
        line = list(map(int, line))
        for i in range(len(line)):
            for j in range(i+1, len(line)):
                if line[i] % line[j] == 0:
                    sum += (line[i] / line[j])
                elif line[j] % line[i] == 0:
                    sum += (line[j] / line[i])
    return int(sum)

def compute_checksums2_p2(numbers: List[List[int]]) -> int:
    sum = 0
    for num_list in numbers:
        lst_len = len(num_list)
        for i in range(lst_len):
            for j in range(i+1, lst_len):
                if num_list[i] % num_list[j] == 0:
                    sum += (num_list[i] / num_list[j])
                elif num_list[j] % num_list[i] == 0:
                    sum += (num_list[j] / num_list[i])
    return int(sum) 

"""
assert compute_checksums2(['5 9 2 8']) == 4
assert compute_checksums2(['9 4 7 3']) == 3
assert compute_checksums2(['3 8 6 5']) == 2
"""
#print(input_text)
#print(input_text2)
result = compute_checksums_p2(input_text)
result2 = compute_checksums2_p2(input_text2)
print(result, result2)