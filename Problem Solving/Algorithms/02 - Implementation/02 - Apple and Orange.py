# ==============================
#         Information
# ==============================

# Title: 02 - Apple and Orange
# Link: https://www.hackerrank.com/challenges/apple-and-orange/problem
# Difficulty: Easy
# Max Score: 10
# Language: Python

# ==============================
#         Solution
# ==============================

def countApplesAndOranges(s, t, a, b, apples, oranges):

    # 1. iterate through apples and in every element, add the value of the apple's location
    # 2. using the apple's location values, check every apple if it is inside the houses range
    # 3. get the number of apple that is inside the house's range
    # 4. repeat 1-3 for oranges or in every step of apple, do the same for oranges
    # 5. print the number of apples and oranges that's inside the house's range

    apples_location = [i+a for i in apples]
    oranges_location = [i+b for i in oranges]
    apples_count = 0
    oranges_count = 0

    for i in apples_location:
        if s <= i <= t:
            apples_count += 1

    for i in oranges_location:
        if s <= i <= t:
            oranges_count += 1

    print(apples_count)
    print(oranges_count)


if __name__ == '__main__':
    st = input().split()

    s = int(st[0])

    t = int(st[1])

    ab = input().split()

    a = int(ab[0])

    b = int(ab[1])

    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)
