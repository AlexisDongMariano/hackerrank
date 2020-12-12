# ==============================
#         Information
# ==============================

# Title: 01 - collections.Counter()
# Link: https://www.hackerrank.com/challenges/collections-counter/problem
# Difficulty: Easy
# Max Score: 10
# Language: Python

# ==============================
#         Solution
# ==============================


# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter

shoe_sizes = int(input())
sizes = Counter(list(map(int, (input()).split(' '))))
no_of_customers = int(input())

orders = []
for i in range(no_of_customers):
    # order is key value pair where first item is the order size and the amount as second
    orders.append(tuple(map(int, (input()).split(' '))))

total = 0
for order in orders:
    if order[0] in list(sizes.keys()):
        order_size = order[0]
        if sizes[order_size] > 0:
            sizes[order_size] = sizes[order_size] - 1
            total += order[1]
            
print(total)
