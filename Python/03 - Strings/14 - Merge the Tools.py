# ==============================
#         Information
# ==============================

# Title: 14 - Merge the Tools!
# Link: https://www.hackerrank.com/challenges/merge-the-tools/problem
# Difficulty: Medium
# Max Score: 40
# Language: Python

# ==============================
#         Solution
# ==============================


def merge_the_tools(string, k):
    # your code goes here
    sub_str = []
    output_str = ''

    for index, letter in enumerate(string, 1):
        if letter not in sub_str:
            sub_str.append(letter)

        if index % k == 0:
            output_str += ''.join(sub_str) + '\n'
            sub_str = []

    print(output_str)


if __name__ == '__main__':
    string, k = raw_input(), int(raw_input())
    merge_the_tools(string, k)
