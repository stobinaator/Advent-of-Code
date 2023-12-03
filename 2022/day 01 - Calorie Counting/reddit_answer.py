data = open('input.txt').read().split("\n\n")

vals = sorted([sum([int(l) for l in group.split("\n")]) for group in data], reverse=True)

print(vals[0])
print(sum(vals[:3]))