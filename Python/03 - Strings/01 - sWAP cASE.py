# ==============================
#         Information
# ==============================

# Title: 01 - sWAP cASE
# Link: https://www.hackerrank.com/challenges/swap-case/problem
# Difficulty: Easy
# Max Score: 10
# Language: Python

# ==============================
#         Solution
# ==============================


def swap_case(s):
    return s.swapcase()


if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)