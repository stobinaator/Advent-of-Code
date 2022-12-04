"""
--- Day 4: Camp Cleanup ---
Space needs to be cleared before the last supplies can be unloaded from the ships, and so several Elves have been assigned the job of cleaning up sections of the camp. Every section has a unique ID number, and each Elf is assigned a range of section IDs.

However, as some of the Elves compare their section assignments with each other, they've noticed that many of the assignments overlap. To try to quickly find overlaps and reduce duplicated effort, the Elves pair up and make a big list of the section assignments for each pair (your puzzle input).

For example, consider the following list of section assignment pairs:

2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8
For the first few pairs, this list means:

Within the first pair of Elves, the first Elf was assigned sections 2-4 (sections 2, 3, and 4), while the second Elf was assigned sections 6-8 (sections 6, 7, 8).
The Elves in the second pair were each assigned two sections.
The Elves in the third pair were each assigned three sections: one got sections 5, 6, and 7, while the other also got 7, plus 8 and 9.
This example list uses single-digit section IDs to make it easier to draw; your actual list might contain larger numbers. Visually, these pairs of section assignments look like this:

.234.....  2-4
.....678.  6-8

.23......  2-3
...45....  4-5

....567..  5-7
......789  7-9

.2345678.  2-8
..34567..  3-7

.....6...  6-6
...456...  4-6

.23456...  2-6
...45678.  4-8
Some of the pairs have noticed that one of their assignments fully contains the other. For example, 2-8 fully contains 3-7, and 6-6 is fully contained by 4-6. In pairs where one assignment fully contains the other, one Elf in the pair would be exclusively cleaning sections their partner will already be cleaning, so these seem like the most in need of reconsideration. In this example, there are 2 such pairs.

In how many assignment pairs does one range fully contain the other?

--- Part Two ---
It seems like there is still quite a bit of duplicate work planned. Instead, the Elves would like to know the number of pairs that overlap at all.

In the above example, the first two pairs (2-4,6-8 and 2-3,4-5) don't overlap, while the remaining four pairs (5-7,7-9, 2-8,3-7, 6-6,4-6, and 2-6,4-8) do overlap:

5-7,7-9 overlaps in a single section, 7.
2-8,3-7 overlaps all of the sections 3 through 7.
6-6,4-6 overlaps in a single section, 6.
2-6,4-8 overlaps in sections 4, 5, and 6.
So, in this example, the number of overlapping assignment pairs is 4.

In how many assignment pairs do the ranges overlap?
"""

RAW = """2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8
"""

raw_sections = [[[int(sec) for sec in section.split("-")] for section in sections.split(",")] for sections in RAW.strip().split("\n")]
print(raw_sections)

input = [[[int(sec) for sec in section.split("-")] for section in sections.split(",")] for sections in open("input.txt").read().strip().split("\n")]

def check_if_sections_overlap(sections):
    overlapping_sections = 0
    for section in sections:
        left_section = section[0]
        right_section = section[1]
        if len(left_section) > len(right_section):
            if left_section[0] <= right_section[0] and left_section[-1] >= right_section[-1]:
                overlapping_sections += 1
        elif len(left_section) < len(right_section):
            if left_section[0] >= right_section[0] and left_section[-1] <= right_section[-1]:
                overlapping_sections += 1
        else:
            if left_section == right_section:
                overlapping_sections += 1
            elif left_section[0] >= right_section[0] and left_section[-1] <= right_section[-1]:
                overlapping_sections += 1
            elif left_section[0] <= right_section[0] and left_section[-1] >= right_section[-1]:
                overlapping_sections += 1
    return overlapping_sections


assert check_if_sections_overlap([[[1,1], [1,1]]]) == 1
assert check_if_sections_overlap([[[1,2,3,4], [2,3]]]) == 1
assert check_if_sections_overlap([[[2,3], [1,2,3,4]]]) == 1
assert check_if_sections_overlap([[[2,4], [6,8]]]) == 0
assert check_if_sections_overlap(raw_sections) == 2

part1 = check_if_sections_overlap(input)
print(part1)

def create_ranges(section):
    new_section = []
    for i in range(section[0], section[-1]+1):
        new_section.append(i)
    return new_section

def check_for_full_overlap(sections):
    fully_overlapping_sections = 0
    for section in sections:
        left_section = section[0]
        right_section = section[1]
        left = create_ranges(left_section)
        right = create_ranges(right_section)
        if len(set(left) & set(right)) > 0:
            fully_overlapping_sections += 1
    return fully_overlapping_sections

assert check_for_full_overlap(raw_sections) == 4

part2 = check_for_full_overlap(input)
print(part2)