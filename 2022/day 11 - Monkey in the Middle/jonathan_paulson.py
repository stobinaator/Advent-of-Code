from copy import deepcopy

data = open("input.txt").read().strip()

M = []
OP = []
DIV = []
TRUE = []
FALSE = []
for monkey in data.split('\n\n'):
    id_, items, op, test, true, false = monkey.split('\n')
    M.append([int(i) for i in items.split(':')[1].split(',')])
    words = op.split()
    op = ''.join(words[-3:])
    # the last 3 words of the input are a valid python function of the single variable "old"
    OP.append(lambda old,op=op:eval(op))
    DIV.append(int(test.split()[-1]))
    TRUE.append(int(true.split()[-1]))
    FALSE.append(int(false.split()[-1]))

START = deepcopy(M)
# Want to know for each item if it is divisible by e.g. 23,19,13,17
# If we just wanted to know if its divisible by 23, we can just keep track of the number modulo 23.
# x+a is divisible by 23 iff (x%23)+a is divisible by 23
# x*a is divisible by 23 iff (x%23)*a is divisible by 23
# We can keep track of the number modulo 23*19*13*17
lcm = 1
for x in DIV:
    lcm = (lcm*x)

for part in [1, 2]:
    C = [0 for _ in range(len(M))]
    M = deepcopy(START)
    for t in range(20 if part==1 else 10_000):
        for i in range(len(M)):
            for item in M[i]:
                C[i] += 1
                item = OP[i](item)
                if part == 2:
                    item %= lcm
                if part == 1:
                    item = (item // 3)
                if item % DIV[i] == 0:
                    M[TRUE[i]].append(item)
                else:
                    M[FALSE[i]].append(item)
            M[i] = []
    print(sorted(C)[-1] * sorted(C)[-2])
