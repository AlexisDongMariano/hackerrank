# ==============================
#         Information
# ==============================

# Title: 08 - Text Wrap
# Link: https://www.hackerrank.com/challenges/text-wrap/problem
# Difficulty: Easy
# Max Score: 10
# Language: Python

# ==============================
#         Solution
# ==============================

import textwrap


def wrap(string, max_width):
    return '\n'.join(textwrap.wrap(string, max_width))


if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
