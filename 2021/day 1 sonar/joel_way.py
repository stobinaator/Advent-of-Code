from typing import List
import os

RAW = """199
200
208
210
200
207
240
269
260
263"""

input = [int(x) for x in RAW.split('\n')]

def count_increases(depths: List[int], gap: int = 1) -> int:
    count = 0
    for i in range(len(depths) - gap):
        if depths[i] < depths[i + gap]:
            count += 1
    return count

assert count_increases([1,2,3]) == 2
assert count_increases(input) == 7

assert count_increases(input, gap=3) == 5

if __name__ == "__main__":
    cd = os.path.abspath(os.getcwd())
    with open(f'{cd}/input.txt', 'r') as f:
        raw = f.read()
    input = [int(x) for x in raw.split('\n')]
    print(count_increases(input))
    print(count_increases(input, gap=3))