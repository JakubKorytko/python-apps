import os

dir = os.path.dirname(__file__)

for i in range(1, 4):
    file = os.path.join(dir, "Zadanie " + str(i) + ".py")
    data = open(file).read()

    exec(data)
    print("\n---\n")