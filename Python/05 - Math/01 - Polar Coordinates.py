# ==============================
#         Information
# ==============================

# Title: 01 - Polar Coordinates
# Link: https://www.hackerrank.com/challenges/polar-coordinates/problem
# Difficulty: Easy
# Max Score: 10
# Language: Python

# ==============================
#         Solution
# ==============================


from cmath import phase, polar

polar_points = polar(complex(input()))

print(polar_points[0])
print(polar_points[1])