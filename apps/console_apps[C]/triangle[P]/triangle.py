print("\nWelcome to the triangle creator app!")
print("Please enter the sides of the triangle to check if you can create it\n")

triangle = {
    "a": input("Enter the first side of the triangle: "),
    "b": input("Enter the second side of the triangle: "),
    "c": input("Enter the third side of the triangle: ")
}

try:
    triangle["a"] = float(triangle["a"])
    triangle["b"] = float(triangle["b"])
    triangle["c"] = float(triangle["c"])
except ValueError:
    print("\nSides of the triangle must be numbers!")
    exit()

if (triangle["a"]<0 or triangle["b"]<0 or triangle["c"]<0):
    print("\nSides of the triangle cannot be negative!")
else:
    
    bool_1 = triangle["a"]**2+triangle["b"]**2==triangle["c"]**2
    bool_2 = triangle["a"]**2+triangle["c"]**2==triangle["b"]**2
    bool_3 = triangle["b"]**2+triangle["c"]**2==triangle["a"]**2

    maxValue = max(max(triangle, key = lambda k: triangle[k]))
    maxKey = triangle[maxValue]

    del triangle[maxValue]
    rest = list(triangle.values())

    is_triangle = maxKey<rest[0]+rest[1]

    str_add = ""

    if (bool_1 or bool_2 or bool_3):
        str_add = "right-angled "

    if (is_triangle):
        print("\nYou can create a "+str_add+"triangle from these sides")
    else:
        print("\nYou cannot create a triangle from these sides")
