print ("\nWelcome to the program that checks if a point belongs to a straight line\n")

line = {
    "a": input("Please enter A of the straight line equation: "),
    "b": input("Enter B of the straight line equation: ")
}

point = {
    "x": input("Enter X of the point: "),
    "y": input("Enter Y of the point: ")
}

try:
    point["x"] = float(point["x"])
    point["y"] = float(point["y"])
    line["a"] = float(line["a"])
    line["b"] = float(line["b"])
except ValueError:
    print("\nPlease enter numbers only")
    exit()

is_valid = point["y"]==line["a"]*point["x"]+line["b"]

if (is_valid):
    print("\nPoint belongs to the line")
else:
    print("\nPoint does not belong to the line")
