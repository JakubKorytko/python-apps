""" A program that checks if you can create a triangle from the given sides. """

from sys import exit as sys_exit

def read_triangle():
    """ Reads the triangle sides from the user input and returns them in a dictionary """

    triangle = {
        "a": input("Enter the first side of the triangle: "),
        "b": input("Enter the second side of the triangle: "),
        "c": input("Enter the third side of the triangle: ")
    }

    return triangle

def validate_triangle(triangle):
    """ Validates the input """

    try:
        triangle["a"] = float(triangle["a"])
        triangle["b"] = float(triangle["b"])
        triangle["c"] = float(triangle["c"])
    except ValueError:
        print("\nSides of the triangle must be numbers!")
        sys_exit()

def are_triangle_sides_positive(triangle):
    """ Checks if the sides of the triangle are positive """

    return triangle["a"] > 0 and triangle["b"] > 0 and triangle["c"] > 0

def pythagoras_theorem_apply(triangle):
    """ Checks if the Pythagoras theorem applies to the triangle """

    a_squared = triangle["a"]**2
    b_squared = triangle["b"]**2
    c_squared = triangle["c"]**2

    a_2 = b_squared + c_squared == a_squared
    b_2 = a_squared + c_squared == b_squared
    c_2 = a_squared + b_squared == c_squared

    return a_2 or b_2 or c_2

def is_one_side_shorter_than_the_sum_of_the_others(triangle):
    """ Checks if one side is shorter than the sum of the other two """

    max_value = max(triangle)
    max_key = triangle[max_value]

    triangle_copy = triangle.copy()

    del triangle_copy[max_value]
    rest = list(triangle_copy.values())

    is_longer = max_key < rest[0] + rest[1]

    return is_longer

print("\nWelcome to the triangle creator app!")
print("Please enter the sides of the triangle to check if you can create it\n")

TRIANGLE = read_triangle()

validate_triangle(TRIANGLE)

if not are_triangle_sides_positive(TRIANGLE):
    print("\nSides of the triangle must be positive!")
    sys_exit()

if is_one_side_shorter_than_the_sum_of_the_others(TRIANGLE):
    print("\nYou can create a", end=" ")

    if pythagoras_theorem_apply(TRIANGLE):
        print("right-angled", end=" ")

    print("triangle from these sides")
else:
    print("\nYou cannot create a triangle from these sides")
