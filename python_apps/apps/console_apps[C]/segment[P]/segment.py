""" Module for calculating the distance of a point from a segment by the equation of a line. """

from math import sqrt
from sys import exit as sys_exit


def distance(segment, point):
    """Calculates the distance of a point from a segment by the equation of a line."""

    tab = straight_line_equation(segment)

    return abs((tab[0] * point["x"]) - point["y"] + tab[1]) / sqrt(tab[0] ** 2 + 1)


def straight_line_equation(segment):
    """Calculates the straight line equation."""

    equation_a = (segment["y_b"] - segment["y_a"]) / (segment["x_b"] - segment["x_a"])
    equation_b = segment["y_a"] - equation_a * segment["x_a"]
    return [equation_a, equation_b]


def get_coords():
    """Gets coordinates from the user input"""

    print("\nEnter the coordinates of the point A")

    point = {"x": input("x: "), "y": input("y: ")}

    print("\nEnter the coordinates of the segment:")

    segment = {
        "x_a": input("x of A point: "),
        "y_a": input("y of A point: "),
        "x_b": input("x of B point: "),
        "y_b": input("y of B point: "),
    }

    return point, segment


def validate(point, segment):
    """Validates the input"""

    try:
        point["x"] = float(point["x"])
        point["y"] = float(point["y"])

        segment["x_a"] = float(segment["x_a"])
        segment["y_a"] = float(segment["y_a"])
        segment["x_b"] = float(segment["x_b"])
        segment["y_b"] = float(segment["y_b"])

    except ValueError:
        print("\nYou need to enter the numbers!")
        sys_exit()


def is_a_valid_segment(segment):
    """Checks if the segment is a point"""

    return not (segment["x_a"] == segment["x_b"] and segment["y_a"] == segment["y_b"])


def calculate_distance(point, segment):
    """Calculates the distance of a point from a segment by the equation of a line."""

    return distance(segment, point)


def point_is_on_the_segment(point, segment):
    """Checks if a point is on the segment.
    False means that the point is on the line created by the segment if the distance is 0.
    """

    x_axis = point["x"] >= min(segment["x_a"], segment["x_b"]) and point["x"] <= max(
        segment["x_a"], segment["x_b"]
    )

    y_axis = point["y"] >= min(segment["y_a"], segment["y_b"]) and point["y"] <= max(
        segment["y_a"], segment["y_b"]
    )

    if x_axis and y_axis:
        return True

    return False


print(
    "\nThis is a module with functions for calculating the distance of a point", end=" "
)
print("from a segment by the equation of a line.")

[POINT, SEGMENT] = get_coords()
validate(POINT, SEGMENT)

if not is_a_valid_segment(SEGMENT):
    print("Its not a segment, its a point!")

else:
    dist = calculate_distance(POINT, SEGMENT)

    if dist == 0:
        if point_is_on_the_segment(POINT, SEGMENT):
            print("\nPoint is on the segment!")

        else:
            print(
                "\nPoint is not on the segment but is on the line created by the segment!"
            )
    else:
        print("\nDistance from point to the line created by the segment is: ", dist)
