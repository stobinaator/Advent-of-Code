import os 
cd = os.path.abspath(os.getcwd())

def fuel(mass: int) -> int:
    return mass // 3 - 2

assert fuel(12) == 2
assert fuel(14) == 2
assert fuel(1969) == 654
assert fuel(100756) == 33583

with open(f'{cd}/input.txt') as f:
    masses = [int(line.strip()) for line in f]
    part1 = sum(fuel(mass) for mass in masses)

print(part1)

# for part 2 we add fuel for the fuel
def fuel_for_the_fuel(mass: int) -> int:
    total = 0
    next_fuel = fuel(mass)

    while next_fuel > 0:
        total += next_fuel
        next_fuel = fuel(next_fuel)
    return total
    


assert fuel_for_the_fuel(14) == 2
assert fuel_for_the_fuel(1969) == 966
assert fuel_for_the_fuel(100756) == 50346

part2 = sum(fuel_for_the_fuel(mass) for mass in masses)
print(part2)