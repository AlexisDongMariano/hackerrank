# ==============================
#         Information
# ==============================

# Title: 01 - Introduction to Sets
# Link: https://www.hackerrank.com/challenges/py-introduction-to-sets/problem
# Difficulty: Easy
# Max Score: 10
# Language: Python

# ==============================
#         Solution
# ==============================


def average(array):
    # your code goes here
    return sum(set(array)) / len(set(array))


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)