from typing import Set, List
from collections import Counter
import os 

cd = os.path.abspath(os.getcwd())

with open(f'{cd}/input.txt') as f:
    ids = [line.strip() for line in f]

def char_count_values(word: str) -> Set[int]:
    char_counts = Counter(word)
    return set(char_counts.values())

assert char_count_values("aaabccdd") == {1, 2, 3}
assert char_count_values("") == set()

def checksum(ids: List[int]) -> int:
    """
    return (# of strings with a char occuring exactly twice)*
           (# of strings with a char occuring exactly thrice)
    """
    num_twos = 0
    num_threes = 0

    for box_id in ids:
        ccv = char_count_values(box_id)
        if 2 in ccv:
            num_twos += 1
        if 3 in ccv:
            num_threes += 1

    return num_twos * num_threes

assert checksum(['abcdef','bababc','abbcde', 'abcccd', 'aabcdd', 'abcdee', 'ababab']) == 12

print(checksum(ids))

# Give a list of ids, exactly 2 differ by exactly one char
# find the remaining chars

def characters_in_common(ids: List[int]) -> str:
    leave_one_outs = Counter()

    for box_id in ids:
        for i in range(len(box_id)):
            leave_one_out = tuple(box_id[:i] + "_" + box_id[(i+1):])
            leave_one_outs[leave_one_out] += 1

    [(best, count), [not_best, not_best_count]] = leave_one_outs.most_common(2)
    assert count == 2
    assert not_best_count == 1
    return "".join(c for c in best if c != "_")

TEST_IDS = ['abcde','fghij','klmno','pqrst', 'fguij', 'axcye','wvxyz']

assert characters_in_common(TEST_IDS) == "fgij"

print(characters_in_common(ids))