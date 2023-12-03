RAW_INPUT = """Player 1 starting position: 2
Player 2 starting position: 8"""

p1 = 2 - 1
p2 = 8 - 1
die = 0


def roll():
    global die
    die += 1
    return die


# dynamic programming
# brute-force + memoization
DP = {}


def count_win(p1, p2, s1, s2):
    """
    Given that A is at position p1 and with score s1, and B is at position p2 with score s2, and A is to move.
    return (# of universes where player A wins, # of universes where player B wins)
    """
    if s1 >= 21:
        return (1, 0)
    if s2 >= 21:
        return (0, 1)
    if (p1, p2, s1, s2) in DP:
        return DP[(p1, p2, s1, s2)]
    ans = (0, 0)
    for d1 in [1, 2, 3]:
        for d2 in [1, 2, 3]:
            for d3 in [1, 2, 3]:
                new_p1 = (p1 + d1 + d2 + d3) % 10
                new_s1 = s1 + new_p1 + 1

                x1, y1 = count_win(p2, new_p1, s2, new_s1)
                # here we do a swap-back
                # because on the preceding line we swapped the players
                ans = (ans[0] + y1, ans[1] + x1)
    DP[(p1, p2, s1, s2)] = ans
    return ans


print(max(count_win(p1, p2, 0, 0)))
assert False

s1 = 0
s2 = 0
while True:
    m1 = roll() + roll() + roll()
    p1 = (p1 + m1) % 10
    s1 += p1 + 1
    if s1 >= 1000:
        print(s2 * die)
        break

    m2 = roll() + roll() + roll()
    p2 = (p2 + m2) % 10
    s2 += p2 + 1
    if s2 >= 1000:
        print(s1 * die)
        break
