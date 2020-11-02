# ==============================
#         Information
# ==============================

# Title: Day 9: Recursion 3
# Link: https://www.hackerrank.com/challenges/30-recursion/problem
# Difficulty: Easy
# Max Score: 30
# Language: Python

# ==============================
#         Solution
# ==============================


def factorial(n):
    if n == 1:
        return 1
    else:
        return factorial(n-1)*n


n = int(input())
print(factorial(n))
