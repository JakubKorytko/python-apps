""" Program that checks if a point belongs to a straight line """

from sys import exit as sys_exit


def get_coords():
    """Gets coordinates from the user input"""

    line = {
        "a": input("Please enter A of the straight line equation: "),
        "b": input("Enter B of the straight line equation: "),
    }

    point = {"x": input("Enter X of the point: "), "y": input("Enter Y of the point: ")}

    return line, point


def validate(line, point):
    """Validates the input"""

    try:
        point["x"] = float(point["x"])
        point["y"] = float(point["y"])
        line["a"] = float(line["a"])
        line["b"] = float(line["b"])
    except ValueError:
        print("\nPlease enter numbers only")
        sys_exit()


def belongs_to_line(line, point):
    """Checks if a point belongs to a line"""

    return point["y"] == line["a"] * point["x"] + line["b"]


print("\nWelcome to the program that checks if a point belongs to a straight line\n")

[LINE, POINT] = get_coords()
validate(LINE, POINT)

if belongs_to_line(LINE, POINT):
    print("\nPoint belongs to the line")
else:
    print("\nPoint does not belong to the line")
