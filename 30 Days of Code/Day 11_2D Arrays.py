# ==============================
#         Information
# ==============================

# Title: Day 11: 2D Arrays
# Link: https://www.hackerrank.com/challenges/30-2d-arrays/problem
# Difficulty: Easy
# Max Score: 30
# Language: Python

# ==============================
#         Solution
# ==============================

# 1. Build the pattern of hourglass
#   1.a. get the top
#   1.b. get the middle
#   1.c. get the bottom
# 2. Scan the array for hourglass patterns from left to right, top to bottom
# 3. in every valid hourglass, get the sum
# 4. return/print the largest sum of an hourglass

def get_max_hourglass_sum(arr):
    top = bottom = hourglass = []
    mid = 0
    # assign lowest value possible to allow negative values
    hourglass_sum = float('-inf')

    for i in range(4):
        for j in range(4):
            if i < 4:
                top = arr[i][j:j+3]
            mid = arr[i+1][j+1]
            if i < 4:
                bottom = arr[i+2][j:j+3]
            hourglass = (top + bottom)
            hourglass.append(mid)
            if sum(hourglass) > hourglass_sum:
                hourglass_sum = sum(hourglass)
    print(hourglass_sum)


if __name__ == '__main__':
    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

get_max_hourglass_sum(arr)
