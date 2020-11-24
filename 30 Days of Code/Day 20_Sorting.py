# ==============================
#         Information
# ==============================

# Title: Day 20: Sorting
# Link: https://www.hackerrank.com/challenges/30-sorting/problem
# Difficulty: Easy
# Max Score: 30
# Language: Python

# ==============================
#         Solution
# ==============================

n = int(input().strip())
a = list(map(int, input().strip().split(' ')))
# Write Your Code Here
total_swap = 0

# Bubble Sort Algorithm
for i in range(len(a)):
    number_of_swaps = 0
    for j in range(len(a)-1):
        if a[j] > a[j+1]:
            a[j], a[j+1] = a[j+1], a[j]
            number_of_swaps += 1
            total_swap += 1

    if number_of_swaps == 0:
        break

print('Array is sorted in', total_swap, 'swaps.')
print('First Element:', a[0])
print('Last Element:', a[len(a)-1])
