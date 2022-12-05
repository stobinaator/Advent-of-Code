"""
--- Day 5: Supply Stacks ---
The expedition can depart as soon as the final supplies have been unloaded from the ships. Supplies are stored in stacks of marked crates, but because the needed supplies are buried under many other crates, the crates need to be rearranged.

The ship has a giant cargo crane capable of moving crates between stacks. To ensure none of the crates get crushed or fall over, the crane operator will rearrange them in a series of carefully-planned steps. After the crates are rearranged, the desired crates will be at the top of each stack.

The Elves don't want to interrupt the crane operator during this delicate procedure, but they forgot to ask her which crate will end up where, and they want to be ready to unload them as soon as possible so they can embark.

They do, however, have a drawing of the starting stacks of crates and the rearrangement procedure (your puzzle input). For example:

    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2
In this example, there are three stacks of crates. Stack 1 contains two crates: crate Z is on the bottom, and crate N is on top. Stack 2 contains three crates; from bottom to top, they are crates M, C, and D. Finally, stack 3 contains a single crate, P.

Then, the rearrangement procedure is given. In each step of the procedure, a quantity of crates is moved from one stack to a different stack. In the first step of the above rearrangement procedure, one crate is moved from stack 2 to stack 1, resulting in this configuration:

[D]        
[N] [C]    
[Z] [M] [P]
 1   2   3 
In the second step, three crates are moved from stack 1 to stack 3. Crates are moved one at a time, so the first crate to be moved (D) ends up below the second and third crates:

        [Z]
        [N]
    [C] [D]
    [M] [P]
 1   2   3
Then, both crates are moved from stack 2 to stack 1. Again, because crates are moved one at a time, crate C ends up below crate M:

        [Z]
        [N]
[M]     [D]
[C]     [P]
 1   2   3
Finally, one crate is moved from stack 1 to stack 2:

        [Z]
        [N]
        [D]
[C] [M] [P]
 1   2   3
The Elves just need to know which crate will end up on top of each stack; in this example, the top crates are C in stack 1, M in stack 2, and Z in stack 3, so you should combine these together and give the Elves the message CMZ.

After the rearrangement procedure completes, what crate ends up on top of each stack?

--- Part Two ---
As you watch the crane operator expertly rearrange the crates, you notice the process isn't following your prediction.

Some mud was covering the writing on the side of the crane, and you quickly wipe it away. The crane isn't a CrateMover 9000 - it's a CrateMover 9001.

The CrateMover 9001 is notable for many new and exciting features: air conditioning, leather seats, an extra cup holder, and the ability to pick up and move multiple crates at once.

Again considering the example above, the crates begin in the same configuration:

    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 
Moving a single crate from stack 2 to stack 1 behaves the same as before:

[D]        
[N] [C]    
[Z] [M] [P]
 1   2   3 
However, the action of moving three crates from stack 1 to stack 3 means that those three moved crates stay in the same order, resulting in this new configuration:

        [D]
        [N]
    [C] [Z]
    [M] [P]
 1   2   3
Next, as both crates are moved from stack 2 to stack 1, they retain their order as well:

        [D]
        [N]
[C]     [Z]
[M]     [P]
 1   2   3
Finally, a single crate is still moved from stack 1 to stack 2, but now it's crate C that gets moved:

        [D]
        [N]
        [Z]
[M] [C] [P]
 1   2   3
In this example, the CrateMover 9001 has put the crates in a totally different order: MCD.

Before the rearrangement process finishes, update your simulation so that the Elves know where they should stand to be ready to unload the final supplies. After the rearrangement procedure completes, what crate ends up on top of each stack?


"""


RAW = """    
    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2
"""

STACK = [
    # first is bottom, last is top
    ["Z", "N"],
    ["M", "C", "D"],
    ["P"]
]

CMDS = """move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2
""".strip().split("\n")

def move_crates(cmds, stack, pt):
    for cmd in cmds:
        words = cmd.split()
        quantity, from_, to_ = int(words[1]), int(words[3]), int(words[5])
        to_be_moved = stack[from_-1][-quantity:]
        if len(to_be_moved) == 1:
            stack[to_-1].append(to_be_moved[0])
            stack[from_-1].pop()
        else:
            if pt == 1:
                to_be_moved = reversed(to_be_moved)
            for to_move in to_be_moved:
                stack[to_-1].append(to_move)
                stack[from_-1].pop()
    return stack    

# crates_on_top_p1 = "".join(s[-1] for s in move_crates(CMDS, STACK, pt=1) if len(s) > 0)
# assert crates_on_top_p1 == "CMZ"

# crates_on_top_p2 = "".join(s[-1] for s in move_crates(CMDS, STACK, pt=2) if len(s) > 0)
# assert crates_on_top_p2 == "MCD"

input_stack = [
    ["G", "F", "V", "H", "P", "S"],
    ["G", "J", "F", "B" ,"V" ,"D" ,"Z" ,"M"],
    ["G", "M", "L", "J", "N"],
    ["N", "G", "Z", "V", "D", "W", "P"],
    ["V", "R", "C", "B"],
    ["V", "R", "S", "M", "P", "W", "L", "Z"],
    ["T", "H", "P"],
    ["Q", "R", "S", "N", "C", "H", "Z", "V"],
    ["F", "L", "G", "P", "V", "Q", "J"]
]
input_cmds = open("input.txt").read().strip().split("\n")


crates_on_top_p1 = "".join(s[-1] for s in move_crates(input_cmds, input_stack, pt=1))
print(crates_on_top_p1)
crates_on_top_p2 = "".join(s[-1] for s in move_crates(input_cmds, input_stack, pt=2))
print(crates_on_top_p2)
