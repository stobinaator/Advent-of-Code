# https://youtu.be/XVEP2d5esmY?list=PLeDtc0GP5IClpoQ6ZnsIk8nzNHaoR76hh

import os

cd = os.path.abspath(os.getcwd())

def read_sequence() -> list:
    with open(f"{cd}/input.txt", "r") as f:
        data = f.readline()
        data = data.replace('\n', '')
    return data

def sum_matching_digits(s: str) -> int:
    total = 0

    for curr_val , next_val in zip(s, s[1:]):
        if curr_val == next_val:
            total += int(curr_val)

    if s[0] == s[-1]:
        total += int(s[0])

    return total


assert sum_matching_digits("1122") == 3
assert sum_matching_digits("1111") == 4
assert sum_matching_digits("1234") == 0
assert sum_matching_digits("91212129") == 9

def sum_matching_digits_halfway(s: str) -> int:
    length = len(s)
    halfway = length//2
    total = 0

    for curr_val , next_val in zip(s, s[halfway:]):
        if curr_val == next_val:
            total += 2 * int(curr_val)

    return total

assert sum_matching_digits_halfway("1212") == 6
assert sum_matching_digits_halfway("1221") == 0
assert sum_matching_digits_halfway("123425") == 4
assert sum_matching_digits_halfway("123123") == 12
assert sum_matching_digits_halfway("12131415") == 4