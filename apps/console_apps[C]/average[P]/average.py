""" App to calculate grade point average """

import re
import os

def error(grade):
    """ Prints an error message and exits the program."""

    print("\nFile contains invalid grade: "+grade+" (must be a number between 1 and 6)")
    print("Exiting...")
    exit()

print("\nWelcome to the grade point average calculator!")
print("Please keep in mind that the grades (floats are also accepted) must be between 1 and 6 and separated by commas")
print("This program will look for them in the file named \"grades.txt\" in file directory")
print("(But you can enter them manually if you wish to)\n")
print("Searching for \"grades.txt\" file...")

text = ""

if (os.path.exists("grades.txt")):
    f = open("grades.txt", "r")
    print("file found!")
    text = f.read()
else:
    answer = input("file not found, do you wish to enter the grades manually? (y/n):")
    while (answer != "y" and answer != "n"):
        answer = input()
    if (answer=="n"):
        print("\nExiting...")
        exit()
    elif (answer=="y"):
        text = input("\nEnter the grades separated by commas: ")


text = re.sub("\s+", "", text)
grades = text.split(",")

sum = 0

grades_length = len(grades)
for grade in grades:

    try:
        grade = float(grade)
    except ValueError:
        error(grade)

    if (grade<1 or grade>6):
        error(grade)
        
    sum+=grade

avg = sum/grades_length
gradePoint = ("\nGrade point average is "+str(round(avg,2)))

if (avg>=2):
    print(gradePoint,"you passed!")
else:
    print(gradePoint,"you didn't pass yet!")