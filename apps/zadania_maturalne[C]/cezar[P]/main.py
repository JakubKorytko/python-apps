import os

dir = os.path.dirname(__file__)

for i in range(1, 4):
    file = os.path.join(dir, "Zadanie 6." + str(i) + ".py")
    data = open(file).read()

    exec(data)

print("Wyniki znajduja sie w folderze 'wyniki' w plikach: 'wyniki_6_1.txt', 'wyniki_6_2.txt', 'wyniki_6_3.txt")