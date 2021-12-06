import os
from typing import List, Iterator, Set

cd = os.path.abspath(os.getcwd())

with open(f'{cd}/input.txt', 'r') as f:
    numbers = [int(num.strip()) for num in f]

print(sum(numbers))

def all_freqencies(numbers: List[int], start: int = 0) -> Iterator[int]:
    """
    Generate all frequencies by adding the numbers in a cycle
    """
    frequency = start

    while True:
        for number in numbers:
            yield frequency
            frequency += number

def first_repeat_frequency(numbers: List[int], start: int = 0) -> int:
    seen = set()
    for freq in all_freqencies(numbers, start):
        if freq in seen:
            return freq
        else:
            seen.add(freq)

assert first_repeat_frequency([1, -1]) == 0
assert first_repeat_frequency([3, 3, 4, -2, -4]) == 10
assert first_repeat_frequency([-6, 3, 8, 5, -6]) == 5
assert first_repeat_frequency([7, 7, -2, -7, -4]) == 14

print(first_repeat_frequency(numbers))
