# ==============================
#         Information
# ==============================

# Title: 01 - itertools.product()
# Link: https://www.hackerrank.com/challenges/itertools-product/problem
# Difficulty: Easy
# Max Score: 10
# Language: Python

# ==============================
#         Solution
# ==============================


# itertools.product()
# This tool computes the cartesian product of input iterables.
# It is equivalent to nested for-loops.
# For example, product(A, B) returns the same as ((x,y) for x in A for y in B).

from itertools import product

# take inputs, convert to int and stack in a list/array
list_a = list(map(int, (input()).split(' ')))
list_b = list(map(int, (input()).split(' ')))

# apply the cartesian product, convert into str, and join each tuple with a space
print(' '.join(map(str, product(list_a, list_b))))
