# ==============================
#         Information
# ==============================

# Title: 06 - Tuples
# Link: https://www.hackerrank.com/challenges/python-tuples/problem
# Difficulty: Easy
# Max Score: 10
# Language: Python

# ==============================
#         Solution
# ==============================

# accept number of inputs
n = int(input())
# map the input to integer and convert to tuple
integer_list = tuple(map(int, input().split()))

print(hash(integer_list))