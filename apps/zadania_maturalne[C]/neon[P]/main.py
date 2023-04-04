import os

dir = os.path.dirname(__file__)

for i in range(1, 5):
    file = os.path.join(dir, "Zadanie 4." + str(i) + ".py")
    data = open(file).read()

    exec(data)