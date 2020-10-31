# ==============================
#         Information
# ==============================

# Title: 09 - Designer Door Mat
# Link: https://www.hackerrank.com/challenges/designer-door-mat/problem
# Difficulty: Easy
# Max Score: 10
# Language: Python

# ==============================
#         Solution
# ==============================


# enter width and length dimension of the map
width, length = map(int, input().split(' '))
design = '.|.'

count = 1
for i in range(1, (width//2)+1):
    print((count*design).center(length, '-'))
    count += 2
print('WELCOME'.center(length, '-'))

count -= 2
for i in range((width//2), 0, -1):
    print((count*design).center(length, '-'))
    count -= 2


# ==============================
#         Example Input
# ==============================

7 21


# ==============================
#         Example Output
# ==============================
# ---------.|.---------
# ------.|..|..|.------
# ---.|..|..|..|..|.---
# -------WELCOME-------
# ---.|..|..|..|..|.---
# ------.|..|..|.------
# ---------.|.---------
