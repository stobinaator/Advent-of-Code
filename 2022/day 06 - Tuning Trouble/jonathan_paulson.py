input = open("input.txt").read().strip()

p1 = False
p2 = False
for i in range(len(input)):
    if (not p1) and i-3>=0 and len(set([input[i-j] for j in range(4)])) == 4:
        print(i+1)
        p1 = True
    if (not p2) and i-13>=0 and len(set([input[i-j] for j in range(14)])) == 14:
        print(i+1)
        p2 = True
