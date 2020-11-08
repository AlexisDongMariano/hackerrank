# ==============================
#         Information
# ==============================

# Title: 12 - Capitalize!
# Link: https://www.hackerrank.com/challenges/capitalize/problem
# Difficulty: Easy
# Max Score: 20
# Language: Python

# ==============================
#         Solution
# ==============================


def solve(s):
    out = s[0].upper()
    for i in range(1, len(s)):
        if s[i].isalpha() and s[i-1] == ' ':
            out += s[i].upper()
        else:
            out += s[i]
    return out


print(solve(input()))


# ==============================
#         Tips
# ==============================
# we can also use the python string function title()
