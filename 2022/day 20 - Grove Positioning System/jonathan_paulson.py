from collections import deque
data = open("input.txt").read().strip().splitlines()

def solve(data, part):
    X = [int(x) for x in data]
    if part == 2:
        X = [x*811589153 for x in X]
    X = deque(list(enumerate(X)))
    for t in range(10 if part == 2 else 1):
        for i in range(len(X)):
            for j in range(len(X)):
                if X[j][0] == i:
                    break
            while X[0][0] != i:
                X.append(X.popleft())
            val = X.popleft()
            to_pop = val[1]
            to_pop %= len(X)
            
            for _ in range(to_pop):
                X.append(X.popleft())
            X.append(val)

        for j in range(len(X)):
            if X[j][1] == 0:
                break

    print(X[(j+1000)%len(X)][1] + X[(j+2000)%len(X)][1] + X[(j+3000)%len(X)][1])

solve(data, 1)
solve(data, 2)