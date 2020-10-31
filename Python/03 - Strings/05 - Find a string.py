# ==============================
#         Information
# ==============================

# Title: 05 - Find a string
# Link: https://www.hackerrank.com/challenges/find-a-string/problem
# Difficulty: Easy
# Max Score: 10
# Language: Python

# ==============================
#         Solution
# ==============================


def count_substring(string, sub_string):
    count = 0
    end = len(sub_string)

    for i in range(len(string)):
        if string.find(sub_string, i, end) > -1:
            count += 1
        end += 1

    return count


# ==============================
#       Another Solution
# ==============================
def count_substring1(string, sub_string):
    count = 0

    for i in range(len(string)-len(sub_string)+1):
        if sub_string == string[i:i+len(sub_string)]:
            count += 1

    return count


if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print(count)
