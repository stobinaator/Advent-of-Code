from typing import List

Program = List[int]

def run(program: Program) -> None:
    pos = 0

    while program[pos] != 99:
        opcode, loc1, loc2, loc3 = program[pos], program[pos + 1], program[pos + 2], program[pos + 3]
        if opcode == 1:
            program[loc3] = program[loc1] + program[loc2]
        elif opcode == 2:
            program[loc3] = program[loc1] * program[loc2]
        else:
            raise RuntimeError(f"invalid opcode: {program[pos]}")
        
        pos += 4


prog1 = [1,0,0,0,99]; run(prog1); assert prog1 == [2,0,0,0,99]
prog2 = [2,3,0,3,99]; run(prog2); assert prog2 == [2,3,0,6,99]
prog3 = [1,1,1,4,99,5,6,0,99]; run(prog3); assert prog3 == [30,1,1,4,2,5,6,0,99]

def alarm(program: Program, noun: int = 12, verb: int = 2) -> int:
    program = program[:]
    program[1] = noun
    program[2] = verb
    run(program)
    return program[0]

PROGRAM = [1,0,0,3,1,1,2,3,1,3,4,3,1,5,0,3,2,9,1,19,1,19,5,23,1,9,23,27,2,27,6,31,1,5,31,35,2,9,35,39,2,6,39,43,2,43,13,47,2,13,47,51,1,10,51,55,1,9,55,59,1,6,59,63,2,63,9,67,1,67,6,71,1,71,13,75,1,6,75,79,1,9,79,83,2,9,83,87,1,87,6,91,1,91,13,95,2,6,95,99,1,10,99,103,2,103,9,107,1,6,107,111,1,10,111,115,2,6,115,119,1,5,119,123,1,123,13,127,1,127,5,131,1,6,131,135,2,135,13,139,1,139,2,143,1,143,10,0,99,2,0,14,0]

#print(alarm(PROGRAM))
TARGET = 19690720

for noun in range(100):
    for verb in range(100):
        output = alarm(PROGRAM, noun, verb)
        if output == TARGET:
            print(noun, verb, 100*noun+verb)
            break
