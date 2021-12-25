"""--- Day 22: Reactor Reboot ---
Operating at these extreme ocean depths has overloaded the submarine's reactor; it needs to be rebooted.

The reactor core is made up of a large 3-dimensional grid made up entirely of cubes, one cube per integer 3-dimensional coordinate (x,y,z). Each cube can be either on or off; at the start of the reboot process, they are all off. (Could it be an old model of a reactor you've seen before?)

To reboot the reactor, you just need to set all of the cubes to either on or off by following a list of reboot steps (your puzzle input). Each step specifies a cuboid (the set of all cubes that have coordinates which fall within ranges for x, y, and z) and whether to turn all of the cubes in that cuboid on or off.

For example, given these reboot steps:

on x=10..12,y=10..12,z=10..12
on x=11..13,y=11..13,z=11..13
off x=9..11,y=9..11,z=9..11
on x=10..10,y=10..10,z=10..10
The first step (on x=10..12,y=10..12,z=10..12) turns on a 3x3x3 cuboid consisting of 27 cubes

The second step (on x=11..13,y=11..13,z=11..13) turns on a 3x3x3 cuboid that overlaps with the first. 
As a result, only 19 additional cubes turn on; the rest are already on from the previous step

The third step (off x=9..11,y=9..11,z=9..11) turns off a 3x3x3 cuboid that overlaps partially with some cubes that are on, ultimately turning off 8 cubes

The final step (on x=10..10,y=10..10,z=10..10) turns on a single cube, 10,10,10. After this last step, 39 cubes are on.

The initialization procedure only uses cubes that have x, y, and z positions of at least -50 and at most 50. For now, ignore cubes outside this region.

The last two steps are fully outside the initialization procedure area; all other steps are fully within it. After executing these steps in the initialization procedure region, 590784 cubes are on.

Execute the reboot steps. Afterward, considering only cubes in the region x=-50..50,y=-50..50,z=-50..50, how many cubes are on?
code works only with RAW...
-> 615700

-- Part Two ---
Now that the initialization procedure is complete, you can reboot the reactor.

Starting with all cubes off, run all of the reboot steps for all cubes in the reactor.

Consider the following reboot steps:

After running the above reboot steps, 2758514936282235 cubes are on. (Just for fun, 474140 of those are also in the initialization procedure region.)

Starting again with all cubes off, execute all reboot steps. Afterward, considering all cubes, how many cubes are on?
-> 1236463892941356
"""
import os

cd = os.path.abspath(os.getcwd())
raw = open(f"{cd}/input.txt").read()

RAW = """on x=10..12,y=10..12,z=10..12
on x=11..13,y=11..13,z=11..13
off x=9..11,y=9..11,z=9..11
on x=10..10,y=10..10,z=10..10"""

RAW2 = """on x=-20..26,y=-36..17,z=-47..7
on x=-20..33,y=-21..23,z=-26..28
on x=-22..28,y=-29..23,z=-38..16
on x=-46..7,y=-6..46,z=-50..-1
on x=-49..1,y=-3..46,z=-24..28
on x=2..47,y=-22..22,z=-23..27
on x=-27..23,y=-28..26,z=-21..29
on x=-39..5,y=-6..47,z=-3..44
on x=-30..21,y=-8..43,z=-13..34
on x=-22..26,y=-27..20,z=-29..19
off x=-48..-32,y=26..41,z=-47..-37
on x=-12..35,y=6..50,z=-50..-2
off x=-48..-32,y=-32..-16,z=-15..-5
on x=-18..26,y=-33..15,z=-7..46
off x=-40..-22,y=-38..-28,z=23..41
on x=-16..35,y=-41..10,z=-47..6
off x=-32..-23,y=11..30,z=-14..3
on x=-49..-5,y=-3..45,z=-29..18
off x=18..30,y=-20..-8,z=-3..13
on x=-41..9,y=-7..43,z=-33..15
on x=-54112..-39298,y=-85059..-49293,z=-27449..7877
on x=967..23432,y=45373..81175,z=27513..53682"""


def parse(raw: str):
    commands = [line.split(" ")[0] for line in raw.splitlines()]
    coordinates = [line.split(" ")[1].split(",") for line in raw.splitlines()]
    coords = [
        {c.split("=")[0]: c.split("=")[1].split("..") for c in coord_lst}
        for coord_lst in coordinates
    ]
    for lst in coords:
        for k, v in lst.items():
            lst[k] = [int(v[0]), int(v[1])]
    return commands, coords


commands, coords = parse(RAW)
tuples = [[(v[0], v[1]) for _, v in coord.items()] for coord in coords]
# print(tuples)
# print(tuples)
# print(tuples[0])
# print(tuples[0][0])
# print(tuples[0][2][1])

visited_cubes = set()
for i, (curr, next) in enumerate(zip(commands, coords)):
    for x in range(tuples[i][0][0], tuples[i][0][1] + 1):
        for y in range(tuples[i][1][0], tuples[i][1][1] + 1):
            for z in range(tuples[i][2][0], tuples[i][2][1] + 1):

                cube = (x, y, z)

                if curr == "on":
                    if cube not in visited_cubes:
                        visited_cubes.add(cube)
                elif curr == "off":
                    if cube in visited_cubes:
                        visited_cubes.discard(cube)

print(len(visited_cubes))
