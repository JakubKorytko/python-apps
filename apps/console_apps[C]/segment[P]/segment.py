""" Module for calculating the distance of a point from a segment by the equation of a line. """

from math import *

print("\nThis is a module with functions for calculating the distance of a point from a segment by the equation of a line.")

def distance(x_a, y_a, x_b, y_b, x_p, y_p):
    """ Calculates the distance of a point from a segment by the equation of a line. """

    tab = straight_line_equation(x_a, y_a, x_b, y_b)

    return abs((tab[0]*x_p)-y_p+tab[1])/sqrt(tab[0]**2+1)

def straight_line_equation(x_a, y_a, x_b, y_b):
    """ Calculates the straight line equation. """

    a = (y_b - y_a)/(x_b - x_a)
    b = y_a - a * x_a
    return [a,b]

print("\nEnter the coordinates of the point A")

point = {
    "x": input("x: "),
    "y": input("y: ")
}

print("\nEnter the coordinates of the segment:")

segment = {
    "x_a": input("x of A point: "),
    "y_a": input("y of A point: "),
    "x_b": input("x of B point: "),
    "y_b": input("y of B point: ")
}

try:
    point["x"] = float(point["x"])
    point["y"] = float(point["y"])

    segment["x_a"] = float(segment["x_a"])
    segment["y_a"] = float(segment["y_a"])
    segment["x_b"] = float(segment["x_b"])
    segment["y_b"] = float(segment["y_b"])
except ValueError:
    print("\nYou need to enter the numbers!")
    exit()

if(segment["x_a"]==segment["x_b"] and segment["y_a"]==segment["y_b"]):
    print("Its not a segment, its a point!")
else:

    dist = distance(*segment.values(), *point.values())

    if (dist==0):

        x_axis = point["x"] >= min(segment["x_a"], segment["x_b"]) and point["x"] <= max(segment["x_a"], segment["x_b"])
        y_axis = point["y"] >= min(segment["y_a"], segment["y_b"]) and point["y"] <= max(segment["y_a"], segment["y_b"])

        if (x_axis and y_axis):
            print("\nPoint is on the segment!")
        else:
            print("\nPoint is not on the segment but is on the line created by the segment!")
    else:
        print("\nDistance from point to the line created by the segment is: ", dist)
