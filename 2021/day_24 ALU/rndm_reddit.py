def solve(inp, puzzle_input):
    cmds = [line.split() for line in puzzle_input.splitlines()]

    stack = []
    for i in range(14):
        div, chk, add = map(int, [cmds[i * 18 + x][-1] for x in [4, 5, 15]])
        if div == 1:
            stack.append((i, add))
        elif div == 26:
            j, add = stack.pop()
            inp[i] = inp[j] + add + chk
            if inp[i] > 9:
                inp[j] -= inp[i] - 9
                inp[i] = 9
            if inp[i] < 1:
                inp[j] += 1 - inp[i]
                inp[i] = 1

    return "".join(map(str, inp))


if __name__ == "__main__":
    with open("input.txt") as fh:
        data = fh.read()
    print("Part1:", solve([9] * 14, data))
    print("Part2:", solve([1] * 14, data))
