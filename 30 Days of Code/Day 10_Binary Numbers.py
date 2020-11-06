# ==============================
#         Information
# ==============================

# Title: Day 10: Binary Numbers
# Link: https://www.hackerrank.com/challenges/30-binary-numbers/problem
# Difficulty: Easy
# Max Score: 30
# Language: Python

# ==============================
#         Solution
# ==============================

def decimal_to_binary(n, binary):
    '''Convert the decimal to binary as a list passed as an argument. Recursion is used'''
    if n > 1:
        decimal_to_binary(n // 2, binary)
    binary.append(n % 2)


def get_consecutive_binary(n):
    count = 0
    consecutive_one = []
    binary = []
    decimal_to_binary(n, binary)

    # count consecutive 1's in the binary list and append to consecutive_one list once a 0 is
    # the current index, finally, append the count as well if the 2nd to the last index was
    # reached
    for i in range(len(binary)-1):
        if binary[i] == 1 and binary[i+1] == 1:
            count += 1
        if binary[i] == 0:
            consecutive_one.append(count+1)
            count = 0
        if i == len(binary)-2:
            consecutive_one.append(count+1)

    # print the max value of consecutive 1's in the binary list
    print(max(consecutive_one))


if __name__ == '__main__':
    n = int(input())
    get_consecutive_binary(n)
