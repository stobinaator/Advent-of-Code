from collections import Counter

RAW ="""vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw
"""

inputs_raw = RAW.splitlines()




def get_priority(letter) -> int:
    if letter.islower():
        return ord(letter) - 96
    else:
        return ord(letter) - 38

def part1(inputs: list) -> int:
    total_priority = 0

    for rucksack in inputs:
        compartment1, compartment2 = Counter(rucksack[:len(rucksack)//2]), Counter(rucksack[len(rucksack)//2:])
        common = compartment1 & compartment2
        for key, _ in common.items():
            total_priority += get_priority(key)
    return total_priority

def part2(inputs: list) -> int:
    total_priority = 0

    for i in range(2, len(inputs), 3):
        first, second, third = Counter(inputs[i-2]), Counter(inputs[i-1]), Counter(inputs[i])
        common = first & second & third
        total_priority += get_priority(list(common.keys())[0])

    return total_priority


if __name__ == '__main__':
    with open('input.txt') as file:
        inputs = file.read().splitlines()
    print(part1(inputs))
    print(part2(inputs))