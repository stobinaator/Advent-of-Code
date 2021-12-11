"""
--- Day 4: High-Entropy Passphrases ---
A new system policy has been put in place that requires all accounts to use a passphrase instead of simply a password. A passphrase consists of a series of words (lowercase letters) separated by spaces.

To ensure security, a valid passphrase must contain no duplicate words.

For example:

aa bb cc dd ee is valid.
aa bb cc dd aa is not valid - the word aa appears more than once.
aa bb cc dd aaa is valid - aa and aaa count as different words.
The system's full passphrase list is available as your puzzle input. How many passphrases are valid?
3668 is NOT the answer
3323 is NOT the answer
386

--- Part Two ---
For added security, yet another system policy has been put in place. Now, a valid passphrase must contain no two words that are anagrams of each other - that is, a passphrase is invalid if any word's letters can be rearranged to form any other word in the passphrase.

For example:

abcde fghij is a valid passphrase.
abcde xyz ecdab is not valid - the letters from the third word can be rearranged to form the first word.
a ab abc abd abf abj is a valid passphrase, because all letters need to be used when forming another word.
iiii oiii ooii oooi oooo is valid.
oiii ioii iioi iiio is not valid - any of these words can be rearranged to form any other word.
Under this new system policy, how many passphrases are valid?
208
"""

import os
from collections import defaultdict, Counter
from typing import List

cd = os.path.abspath(os.getcwd())

RAW = [ ["aoc", "aco"], # invalid
        ["abcde" ,"fghij"], # valid
        ["abcde" ,"xyz", "ecdab"], # invalid
        ["a" ,"ab" ,"abc" ,"abd", "abf", "abj"], # valid
        ["iiii" ,"oiii", "ooii", "oooi", "oooo"], # valid
        ["oiii" "ioii ""iioi" "iiio"]] # invalid

def part_1(r_input: List[List[str]]) -> int:
    valid_passphrases = 0
    visited_passphrases = []
    for lst in r_input:
        visited_passphrases.clear()
        for word in lst:
            if word not in visited_passphrases:
                visited_passphrases.append(word)
                if len(visited_passphrases) == len(lst):
                    valid_passphrases += 1
            else:
                break
    return valid_passphrases
        
def part_2(r_input: List[List[str]]) -> int:
    valid_passphrases = 0
    visited_passphrases = defaultdict(Counter)
    for lst in r_input:
        visited_passphrases.clear()
        for word in lst:
            if (word not in visited_passphrases) and (Counter(word) not in visited_passphrases.values()):
                visited_passphrases[word] = Counter(word)
                if len(visited_passphrases) == len(lst):
                    valid_passphrases += 1
            else:
                break
    return valid_passphrases


if __name__ == '__main__':
    raw = open(f'{cd}/input.txt').read()
    r_input = [line.split(" ") for line in raw.splitlines()]
    print(part_1(r_input))
    print(part_2(r_input))


