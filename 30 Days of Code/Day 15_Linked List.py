# ==============================
#         Information
# ==============================

# Title: Day 15: Linked List
# Link: https://www.hackerrank.com/challenges/30-linked-list/problem
# Difficulty: Easy
# Max Score: 30
# Language: Python

# ==============================
#         Solution
# ==============================


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Solution:
    def display(self, head):
        current = head
        while current:
            print(current.data, end=' ')
            current = current.next

    def insert(self, head, data):
        # Complete this method
        if head is None:
            head = Node(data)
            self.tail = head
        else:
            node = Node(data)
            self.tail.next = node
            self.tail = node

        return head


mylist = Solution()
T = int(input())
head = None
for i in range(T):
    data = int(input())
    head = mylist.insert(head, data)
mylist.display(head)
