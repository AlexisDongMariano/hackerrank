# ==============================
#         Information
# ==============================

# Title: 13 - The Minion Game
# Link: https://www.hackerrank.com/challenges/the-minion-game/problem
# Difficulty: Medium
# Max Score: 40
# Language: Python

# ==============================
#         Solution
# ==============================


def minion_game(s):
    # summation formula: n * (N + 1) / 2
    total = int(len(s) * (len(s)+1) / 2)
    kevin_count = 0

    for i in range(len(s)):
        if s[i] in 'AEIOU':
            kevin_count += len(s) - i

    if kevin_count > (total - kevin_count):
        print('Kevin', kevin_count)
    elif kevin_count == (total - kevin_count):
        print('Draw')
    else:
        print('Stuart', total-kevin_count)


if __name__ == '__main__':
    s = input()
    minion_game(s)
