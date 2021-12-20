import os
import ast
import re

# https://github.com/jonathanpaulson/AdventOfCode/blob/master/2021/18.py
# https://www.youtube.com/watch?v=EoKjpAIOIOU

cd = os.path.abspath(os.getcwd())
data = open(f"{cd}/input.txt").read().strip()

ans = None


def add(n1, n2):
    ret = [n1, n2]
    return reduce_(ret)


def reduce_(n):
    did1, n1 = explode(n)
    if did1:
        return reduce_(n1)

    did2, n2 = split(n)
    if did2:
        return reduce_(n2)
    else:
        return n2


def explode(n):
    # sourcery no-metrics
    ns = str(n)
    nums = re.findall("\d+", ns)
    parts = []
    i = 0
    while i < len(ns):
        if ns[i] == "[":
            parts.append("[")
            i += 1
        elif ns[i] == ",":
            parts.append(",")
            i += 1
        elif ns[i] == "]":
            parts.append("]")
            i += 1
        elif ns[i] == " ":
            i += 1
        else:
            assert ns[i].isdigit()
            j = i
            while j < len(ns) and ns[j].isdigit():
                j += 1
            parts.append(int(ns[i:j]))
            i = j

    depth = 0
    for i, c in enumerate(parts):
        if c == "[":
            depth += 1
            if depth == 5:
                old_ns = ns
                left = parts[i + 1]
                assert isinstance(left, int)
                assert parts[i + 2] == ","
                right = parts[i + 3]
                assert isinstance(right, int)
                left_i = None
                right_i = None
                for j in range(len(parts)):
                    if isinstance(parts[j], int) and j < i:
                        left_i = j
                    elif isinstance(parts[j], int) and j > i + 3 and right_i is None:
                        right_i = j
                if right_i is not None:
                    assert right_i > i
                    parts[right_i] += right
                parts = parts[:i] + [0] + parts[i + 5 :]
                if left_i is not None:
                    parts[left_i] += left
                return True, ast.literal_eval("".join([str(x) for x in parts]))
        elif c == "]":
            depth -= 1
        else:
            pass
    return False, n


def split(n):
    if isinstance(n, list):
        did1, n1 = split(n[0])
        if did1:
            return True, [n1, n[1]]

        did2, n2 = split(n[1])
        return did2, [n[0], n2]
    else:
        assert isinstance(n, int)
        if n >= 10:
            return True, [n // 2, (n + 1) // 2]
        else:
            return False, n


def magnitude(n):
    if isinstance(n, list):
        return 3 * magnitude(n[0]) + 2 * magnitude(n[1])
    else:
        return n


X = []
for line in data.split("\n"):
    assert line == line.strip()
    X.append(ast.literal_eval(line))

p1 = X[0]
for x in X[1:]:
    p1 = add(p1, x)
print(magnitude(p1))


ans = None
for i in range(len(X)):
    for j in range(i + 1, len(X)):
        x, y = X[i], X[j]
        score = max(magnitude(add(x, y)), magnitude(add(y, x)))
        if ans is None or score > ans:
            ans = score
print(ans)
