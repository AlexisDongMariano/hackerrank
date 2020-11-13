# ==============================
#         Information
# ==============================

# Title: Day 12: Inheritance
# Link: https://www.hackerrank.com/challenges/30-inheritance/problem
# Difficulty: Easy
# Max Score: 30
# Language: Python

# ==============================
#         Solution
# ==============================

class Person:
    def __init__(self, firstName, lastName, idNumber):
        self.firstName = firstName
        self.lastName = lastName
        self.idNumber = idNumber

    def printPerson(self):
        print("Name:", self.lastName + ",", self.firstName)
        print("ID:", self.idNumber)


class Student(Person):
    #   Class Constructor
    #
    #   Parameters:
    #   firstName - A string denoting the Person's first name.
    #   lastName - A string denoting the Person's last name.
    #   id - An integer denoting the Person's ID number.
    #   scores - An array of integers denoting the Person's test scores.
    #
    # Write your constructor here
    def __init__(self, firstName, lastName, idNumber, scores):
        self.firstName = firstName
        self.lastName = lastName
        self.idNumber = idNumber
        self.scores = scores

    #   Function Name: calculate
    #   Return: A character denoting the grade.
    #
    # Write your function here
    def calculate(self):
        rating = ''
        average = sum(self.scores) / len(self.scores)

        if 90 <= average <= 100:
            rating = 'O'
        elif 80 <= average < 90:
            rating = 'E'
        elif 70 <= average < 80:
            rating = 'A'
        elif 55 <= average < 70:
            rating = 'P'
        elif 40 <= average <= 55:
            rating = 'D'
        elif average < 40:
            rating = 'T'

        return rating


line = input().split()
firstName = line[0]
lastName = line[1]
idNum = line[2]
numScores = int(input())  # not needed for Python
scores = list(map(int, input().split()))
s = Student(firstName, lastName, idNum, scores)
s.printPerson()
print("Grade:", s.calculate())