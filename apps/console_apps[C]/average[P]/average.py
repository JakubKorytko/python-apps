""" App to calculate grade point average """

from re import sub as re_sub
from os import path as os_path
from sys import exit as sys_exit

def error(grade):
    """ Prints an error message and exits the program."""

    print("\nFile contains invalid grade: " + str(grade) + " (must be a number between 1 and 6)")
    print("Exiting...")
    sys_exit()

def get_grades():
    """ Gets grades from the file or from the user input """

    grades_path = os_path.join(os_path.dirname(__file__), "grades.txt")

    if os_path.exists(grades_path):

        with open(grades_path, "r", encoding="utf-8") as grades_file:
            print("file found!")
            return grades_file.read()

    answer = input("file not found, do you wish to enter the grades manually? (y/n):")

    while answer not in ("y", "n"):
        answer = input()

    if answer == "y":
        return input("\nEnter the grades separated by commas: ")

    # The answer needs to be "n" here
    print("\nExiting...")
    sys_exit()

def calculate_sum(grades):
    """ Calculates the sum of the grades """

    grades_sum = 0

    for grade in grades:

        try:
            grade = float(grade)
        except ValueError:
            error(grade)

        if (grade < 1 or grade > 6):
            error(grade)

        grades_sum += grade

    return grades_sum

print("\nWelcome to the grade point average calculator!")
print("Please keep in mind that the grades (floats are also accepted)", end=" ")
print("must be between 1 and 6 and separated by commas")
print("This program will look for them in the file named \"grades.txt\" in file directory")
print("(But you can enter them manually if you wish to)\n")
print("Searching for \"grades.txt\" file...")

TEXT = re_sub(r"\s+", "", get_grades())

GRADES = TEXT.split(",")
GRADES_LENGTH = len(GRADES)
GRADES_SUM = calculate_sum(GRADES)

AVG = GRADES_SUM / GRADES_LENGTH

GRADE_POINT = ("\nGrade point average is " + str(round(AVG, 2)))

if AVG >= 2:
    print(GRADE_POINT, "you passed!")
else:
    print(GRADE_POINT, "you didn't pass yet!")
