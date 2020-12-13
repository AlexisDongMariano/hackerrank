# ==============================
#         Information
# ==============================

# Title: 02 - itertools.permutations()
# Link: https://www.hackerrank.com/challenges/itertools-permutations/problem
# Difficulty: Easy
# Max Score: 10
# Language: Python

# ==============================
#         Solution
# ==============================

# This tool returns successive  length permutations of elements in an iterable.
# If  is not specified or is None, then  defaults to the length of the iterable, and all possible full length permutations are generated.
# Permutations are printed in a lexicographic sorted order. So, if the input iterable is sorted, the permutation tuples will be produced in a sorted order.

from itertools import permutations

input_list = (input()).split(' ')
input_str, input_len = input_list[0], int(input_list[1])
permutation_list = list(permutations(input_str, input_len))

for perm in sorted(permutation_list):
    print(''.join(perm))
