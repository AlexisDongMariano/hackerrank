# ==============================
#         Information
# ==============================

# Title: Day 8: Dictionaries and Maps
# Link: https://www.hackerrank.com/challenges/30-dictionaries-and-maps/problem
# Difficulty: Easy
# Max Score: 30
# Language: Python

# ==============================
#         Solution
# ==============================

# accept number of contacts in total
n = int(input())

# input name and contacts separated by space and put in a list
contact_input = [input().split() for _ in range(n)]

# use dictionary comprehension to build a dictionary of contacts
# ex. Dong: 09996815005
contacts = {k:v for k, v in contact_input}

# accept unknown limit of name queries and print the number if it is found
# else, print Not found
while True:
    try:
        query_name = input()
        if query_name in contacts.keys():
            print(f'{query_name}={contacts[query_name]}')
        else:
            print('Not found')
    except:
        break
