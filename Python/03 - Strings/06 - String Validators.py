# ==============================
#         Information
# ==============================

# Title: 06 - String Validators
# Link: https://www.hackerrank.com/challenges/string-validators/problem
# Difficulty: Easy
# Max Score: 10
# Language: Python

# ==============================
#         Solution
# ==============================


def validate_string(s):
    has_alphanumeric = has_alpha = has_digit = has_lower = has_upper = False

    for letter in s:
        if letter.isalnum():
            has_alphanumeric = True
        if letter.isalpha():
            has_alpha = True
        if letter.isdigit():
            has_digit = True
        if letter.islower():
            has_lower = True
        if letter.isupper():
            has_upper = True

    print(has_alphanumeric)
    print(has_alpha)
    print(has_digit)
    print(has_lower)
    print(has_upper)


if __name__ == '__main__':
    s = input()
    validate_string(s)

# ==============================
#       Another Solution
# ==============================
# inp = input()
# print(any(x.isalnum() for x in s))
# print(any(x.isalpha() for x in s))
# print(any(x.isdigit() for x in s))
# print(any(x.islower() for x in s))
# print(any(x.isupper() for x in s))
