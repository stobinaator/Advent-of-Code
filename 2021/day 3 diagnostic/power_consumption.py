"""
--- Day 3: Binary Diagnostic ---
The submarine has been making some odd creaking noises, so you ask it to produce a diagnostic report just in case.

The diagnostic report (your puzzle input) consists of a list of binary numbers which, when decoded properly, can tell you many useful things about the conditions of the submarine. The first parameter to check is the power consumption.

You need to use the binary numbers in the diagnostic report to generate two new binary numbers (called the gamma rate and the epsilon rate). The power consumption can then be found by multiplying the gamma rate by the epsilon rate.

Each bit in the gamma rate can be determined by finding the most common bit in the corresponding position of all numbers in the diagnostic report. For example, given the following diagnostic report:

00100
11110
10110
10111
10101
01111
00111
11100
10000
11001
00010
01010
Considering only the first bit of each number, there are five 0 bits and seven 1 bits. Since the most common bit is 1, the first bit of the gamma rate is 1.

The most common second bit of the numbers in the diagnostic report is 0, so the second bit of the gamma rate is 0.

The most common value of the third, fourth, and fifth bits are 1, 1, and 0, respectively, and so the final three bits of the gamma rate are 110.

So, the gamma rate is the binary number 10110, or 22 in decimal.

The epsilon rate is calculated in a similar way; rather than use the most common bit, the least common bit from each position is used. So, the epsilon rate is 01001, or 9 in decimal. Multiplying the gamma rate (22) by the epsilon rate (9) produces the power consumption, 198.

Use the binary numbers in your diagnostic report to calculate the gamma rate and epsilon rate, then multiply them together. What is the power consumption of the submarine? (Be sure to represent your answer in decimal, not binary.)
4160394
"""
import os
from typing import List, Tuple
from collections import Counter, defaultdict
from itertools import zip_longest, islice

cd = os.path.abspath(os.getcwd())


def conv_input_list(file_path: str) -> List[str]:
    with open(file_path, 'r') as f:
        bins = [binary.strip() for binary in f]
        return bins

def calc_gamma_rate(bins: List) -> Tuple[str, int]:
    bin_len = len(bins[0])
    gamma_bin = str()
    for i in range(bin_len):
        nrs_in_pos_x = [x[i] for x in bins]
        gamma_bin += Counter(nrs_in_pos_x).most_common(1)[0][0][0]

    return gamma_bin, int(gamma_bin, 2)

def calc_epsilon_rate(gamma_bin: str) -> Tuple[str, int]:
    epsilon_bin = str()
    for g_b in gamma_bin:
        epsilon_bin += "1" if g_b == "0" else "0" 
    return epsilon_bin, int(epsilon_bin, 2)

def calc_power_comsumption(gamma_rate: int, epsilon_rate: int) -> int:
    return gamma_rate * epsilon_rate
    
    
def part_1(file_path: str) -> int:
    bins= conv_input_list(file_path)
    gamma_bin, gamma_rate = calc_gamma_rate(bins)
    _, epsilon_rate = calc_epsilon_rate(gamma_bin)
    power_consumption = calc_power_comsumption(gamma_rate, epsilon_rate)
    return power_consumption


#print(part_1(FILE_PATH))

"""
--- Part Two ---
Next, you should verify the life support rating, which can be determined by multiplying the oxygen generator rating by the CO2 scrubber rating.

Both the oxygen generator rating and the CO2 scrubber rating are values that can be found in your diagnostic report - finding them is the tricky part. Both values are located using a similar process that involves filtering out values until only one remains. Before searching for either rating value, start with the full list of binary numbers from your diagnostic report and consider just the first bit of those numbers. Then:

Keep only numbers selected by the bit criteria for the type of rating value for which you are searching. Discard numbers which do not match the bit criteria.
If you only have one number left, stop; this is the rating value for which you are searching.
Otherwise, repeat the process, considering the next bit to the right.
The bit criteria depends on which type of rating value you want to find:

To find oxygen generator rating, determine the most common value (0 or 1) in the current bit position, and keep only numbers with that bit in that position. If 0 and 1 are equally common, keep values with a 1 in the position being considered.
To find CO2 scrubber rating, determine the least common value (0 or 1) in the current bit position, and keep only numbers with that bit in that position. If 0 and 1 are equally common, keep values with a 0 in the position being considered.
For example, to determine the oxygen generator rating value using the same example diagnostic report from above:

Start with all 12 numbers and consider only the first bit of each number. There are more 1 bits (7) than 0 bits (5), so keep only the 7 numbers with a 1 in the first position: 11110, 10110, 10111, 10101, 11100, 10000, and 11001.
Then, consider the second bit of the 7 remaining numbers: there are more 0 bits (4) than 1 bits (3), so keep only the 4 numbers with a 0 in the second position: 10110, 10111, 10101, and 10000.
In the third position, three of the four numbers have a 1, so keep those three: 10110, 10111, and 10101.
In the fourth position, two of the three numbers have a 1, so keep those two: 10110 and 10111.
In the fifth position, there are an equal number of 0 bits and 1 bits (one each). So, to find the oxygen generator rating, keep the number with a 1 in that position: 10111.
As there is only one number left, stop; the oxygen generator rating is 10111, or 23 in decimal.
Then, to determine the CO2 scrubber rating value from the same example above:

Start again with all 12 numbers and consider only the first bit of each number. There are fewer 0 bits (5) than 1 bits (7), so keep only the 5 numbers with a 0 in the first position: 00100, 01111, 00111, 00010, and 01010.
Then, consider the second bit of the 5 remaining numbers: there are fewer 1 bits (2) than 0 bits (3), so keep only the 2 numbers with a 1 in the second position: 01111 and 01010.
In the third position, there are an equal number of 0 bits and 1 bits (one each). So, to find the CO2 scrubber rating, keep the number with a 0 in that position: 01010.
As there is only one number left, stop; the CO2 scrubber rating is 01010, or 10 in decimal.
Finally, to find the life support rating, multiply the oxygen generator rating (23) by the CO2 scrubber rating (10) to get 230.

Use the binary numbers in your diagnostic report to calculate the oxygen generator rating and CO2 scrubber rating, then multiply them together. What is the life support rating of the submarine? (Be sure to represent your answer in decimal, not binary.)
4125600
"""

def calc_oxyg_rating(bins: List) -> Tuple[str, int]:
    bin_len = len(bins[0])
    bins_copy = bins.copy()
    
    for i in range(bin_len):
        nrs_in_pos_x = [x[i] for x in bins_copy]
        
        if len(nrs_in_pos_x) == 1: break
        
        a = list()
        dict_count = Counter(nrs_in_pos_x)
        print(dict_count)
        [a.append(lis) for lis in dict_count.values()]
        if a[0] == a[1]:
            [nrs_in_pos_x.remove(n) for n in nrs_in_pos_x[:] if n == "0"]
            a.clear()
                
        if Counter(nrs_in_pos_x).most_common(1)[0][0] == "1":
            [bins_copy.remove(b) for b in bins_copy[:] if b[i] == "0"]
            
        elif Counter(nrs_in_pos_x).most_common(1)[0][0] == "0":
            [bins_copy.remove(b) for b in bins_copy[:] if b[i] == "1"]
   
    return bins_copy[0], int(bins_copy[0], 2)
                    
            
def calc_co2_rating(bins: List) -> Tuple[str, int]:
    bin_len = len(bins[0])
    bins_copy = bins.copy()
    
    for i in range(bin_len):
        nrs_in_pos_x = [x[i] for x in bins_copy]

        if len(nrs_in_pos_x) == 1: break

        a = list()
        dict_count = Counter(nrs_in_pos_x)
        [a.append(lis) for lis in dict_count.values()]
        if a[0] == a[1]:
            [nrs_in_pos_x.remove(n) for n in nrs_in_pos_x[:] if n == "0"]
            a.clear()

        if Counter(nrs_in_pos_x).most_common(1)[0][0] == "1":
            [bins_copy.remove(b) for b in bins_copy[:] if b[i] == "1"]
            
        elif Counter(nrs_in_pos_x).most_common(1)[0][0] == "0":
            [bins_copy.remove(b) for b in bins_copy[:] if b[i] == "0"]

    return bins_copy[0], int(bins_copy[0], 2)

def calc_lifesupport_rate(oxygen: int, co2: int) -> int:
    return oxygen * co2

FILE_PATH = f'{cd}/ex_input.txt'
bins= conv_input_list(FILE_PATH)
_, ox_rate = calc_oxyg_rating(bins)

_, co2_rate = calc_co2_rating(bins)
res = calc_lifesupport_rate(ox_rate, co2_rate)
print(res)

























"""
PART 1: nice try, but didn't work

def conv_input_str() -> Tuple[str, int]:
    with open(f'{cd}/ex_input.txt', 'r') as f:
        bins = [binary.strip() for binary in f]
        bin_string = str()
        bin_length = 0
        for b in bins:
            bin_length = len(b)
            bin_string += b
        return bin_string, bin_length

def grouper(n, iterable, fillvalue=None):
    "grouper(3, 'ABCDEFG', 'x') --> ABC DEF Gxx"
    args = [iter(iterable)] * n
    return zip_longest(fillvalue=fillvalue, *args)

# for i in range(0, len-step, step):
#  group = list ot i do i+step
def count_occurences(bins: List[str], bin_len: int) -> str:  
    
    dicts = [defaultdict(int) for _ in range(bin_len)]
    
    for i in range(bin_len):
        for j in range(0, len(bins)-bin_len,bin_len):
            print(j)
        #for l in grouper(5, bins):
        #    print(l)
         #   for a in l:
         #       dicts[i][a] += 1
    
    max_val = 0
    new_bin = str()
    
    for i in range(bin_len):
        for _,v in dicts[i].items():
            if v > max_val:
                max_val = v
        dicts[i] = dict(map(reversed, dicts[i].items())) 
        new_bin += dicts[i][max_val]
        max_val = 0
    print(new_bin)
 
def calc_gamma_rate(bins: List) -> Tuple[str, int]:
    bin_len = len(bins[0])
    count_list = list()
    bin_nbrs = str()
    gamma_bin = str()
    
    for i in range(bin_len):
        nrs_in_pos_x = [x[i] for x in bins]
   
        count_list.append(Counter(nrs_in_pos_x).most_common(1))

        bin_nbrs = [c[0][0] for c in count_list]
        
    for n in bin_nbrs:
        gamma_bin += n
    return gamma_bin, int(gamma_bin, 2)
"""