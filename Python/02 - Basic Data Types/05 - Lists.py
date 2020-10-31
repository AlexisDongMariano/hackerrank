# ==============================
#         Information
# ==============================

# Title: 05 - Lists
# Link: https://www.hackerrank.com/challenges/python-lists/problem
# Difficulty: Easy
# Max Score: 10
# Language: Python

# ==============================
#         Solution
# ==============================


def list_insert(index, element, output_list):
    output_list.insert(index, element)

def list_remove(element, output_list):
    output_list.remove(element)

def list_append(element, output_list):
    output_list.append(element)

def list_sort(output_list):
    output_list.sort()

def list_pop(output_list):
    output_list.pop()

def list_reverse(output_list):
    output_list.reverse()


def determine_operation(operation_list, output_list):
    """check the operation based on the first element of the parameter then call the appropriate list operation"""

    operation = operation_list[0]
    if operation == 'insert':
        list_insert(int(operation_list[1]), int(operation_list[2]), output_list)
    elif operation == 'print':
        print(output_list)
    elif operation == 'remove':
        list_remove(int(operation_list[1]), output_list)
    elif operation == 'append':
        list_append(int(operation_list[1]), output_list)
    elif operation == 'sort':
        list_sort(output_list)
    elif operation == 'pop':
        list_pop(output_list)
    elif operation == 'reverse':
        list_reverse(output_list)


# initialize variables
operations = []
operation_list = []
output_list = []

# accept input of operations
n = int(input())

# accept operations in a list
for _ in range(n):
    operations.append(input())

# iterate through the operation inputs and complete each operations
for operation in operations:
    operation_list = operation.split(' ')
    determine_operation(operation_list, output_list)
