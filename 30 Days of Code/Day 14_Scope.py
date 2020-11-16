# ==============================
#         Information
# ==============================

# Title: Day 14: Scope
# Link: https://www.hackerrank.com/challenges/30-scope/problem
# Difficulty: Easy
# Max Score: 30
# Language: Python

# ==============================
#         Solution
# ==============================

class Difference:
    def __init__(self, a):
        self.__elements = a

        # Add your code here
    maximumDifference = 0

    def computeDifference(self):
        for i in self.__elements:
            for j in self.__elements:
                if abs(i-j) > self.maximumDifference:
                    self.maximumDifference = abs(i-j)
# End of Difference class


_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)


# ==============================
#           Tip
# ==============================

# We can also get the maximum value from the list and the minimum value
# subtract them, thus we can get the maximum difference between all the
# elements. This way, we can avoid the Big O(n^2) or factorial time
