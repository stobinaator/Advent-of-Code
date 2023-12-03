"""
--- Day 2: I Was Told There Would Be No Math ---
The elves are running low on wrapping paper, and so they need to submit an order for more. They have a list of the dimensions (length l, width w, and height h) of each present, and only want to order exactly as much as they need.

Fortunately, every present is a box (a perfect right rectangular prism), which makes calculating the required wrapping paper for each gift a little easier: find the surface area of the box, which is 2*l*w + 2*w*h + 2*h*l. The elves also need a little extra paper for each present: the area of the smallest side.

For example:

A present with dimensions 2x3x4 requires 2*6 + 2*12 + 2*8 = 52 square feet of wrapping paper plus 6 square feet of slack, for a total of 58 square feet.
A present with dimensions 1x1x10 requires 2*1 + 2*10 + 2*10 = 42 square feet of wrapping paper plus 1 square foot of slack, for a total of 43 square feet.
All numbers in the elves' list are in feet. How many total square feet of wrapping paper should they order?

--- Part Two ---
The elves are also running low on ribbon. Ribbon is all the same width, so they only have to worry about the length they need to order, which they would again like to be exact.

The ribbon required to wrap a present is the shortest distance around its sides, or the smallest perimeter of any one face. Each present also requires a bow made out of ribbon as well; the feet of ribbon required for the perfect bow is equal to the cubic feet of volume of the present. Don't ask how they tie the bow, though; they'll never tell.

For example:

A present with dimensions 2x3x4 requires 2+2+3+3 = 10 feet of ribbon to wrap the present plus 2*3*4 = 24 feet of ribbon for the bow, for a total of 34 feet.
A present with dimensions 1x1x10 requires 1+1+1+1 = 4 feet of ribbon to wrap the present plus 1*1*10 = 10 feet of ribbon for the bow, for a total of 14 feet.
How many total feet of ribbon should they order?
"""
RAW_wrapping = """2x3x4
1x1x10"""

raw_dimensions = [[int(d) for d in dim.split("x")] for dim in RAW_wrapping.strip().split("\n")]


def calculate_required_wrapping_paper(dimensions: list[int]) -> int:
    length, width, height = dimensions[0], dimensions[1], dimensions[2]
    first, second, third = length * width, width * height, height * length
    smallest_surface = min([first,second, third])
    dims = 2*first + 2*second + 2*third
    return dims + smallest_surface

def total_wrapping_paper(input: list[list[int]]) -> int:
    total = 0
    for dimensions in input:
        total += calculate_required_wrapping_paper(dimensions)
    return total


assert calculate_required_wrapping_paper([2,3,4]) == 58
assert calculate_required_wrapping_paper([1,1,10]) == 43
assert total_wrapping_paper(raw_dimensions) == 101

RAW_ribbon_bow = """2x3x4
1x1x10
"""

raw_dimensions_ribbon_bow = [[int(d) for d in dim.split("x")] for dim in RAW_ribbon_bow.strip().split("\n")]

def calculate_ribbon_and_bow(dimensions: list[int]) -> int:
    length, width, height = dimensions[0], dimensions[1], dimensions[2]
    sorted_list = sorted(dimensions)
    min_one, min_two = sorted_list[0], sorted_list[1]
    ribbon = 2*min_one + 2*min_two
    bow = length * width * height
    return ribbon + bow

def total_feet_ribbon(input: list[list[int]]) -> int:
    total = 0
    for dimensions in input:
        total += calculate_ribbon_and_bow(dimensions)
    return total

assert calculate_ribbon_and_bow([2,3,4]) == 34
assert calculate_ribbon_and_bow([1,1,10]) == 14
assert total_feet_ribbon(raw_dimensions_ribbon_bow) == 48

if __name__ == '__main__':
    input = [[int(d) for d in dim.split("x")] for dim in open("input.txt").read().strip().split("\n")]
    total_paper = total_wrapping_paper(input)
    print(total_paper)
    total_ribbon = total_feet_ribbon(input)
    print(total_ribbon)
        