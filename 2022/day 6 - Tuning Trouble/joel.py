from collections import deque

RAW = """mjqjpqmgbljsphdztnvjfqwrcgsmlb"""

def find_start(packet: str, size: int = 4) -> int:
    q = deque()
    for i, character in enumerate(packet):
        q.append(character)
        if len(q) > size:
            q.popleft()

        if len(set(q)) == size:
            return i+1

    raise ValueError("No start found")


assert find_start(RAW) == 7
assert find_start(RAW, 14) == 19

with open("input.txt") as f:
    raw = f.read()

print(find_start(raw))
print(find_start(raw,14))