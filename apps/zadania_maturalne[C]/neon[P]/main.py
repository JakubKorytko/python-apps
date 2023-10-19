import os
import subprocess

directory = os.path.dirname(__file__)

for i in range(1, 5):
    file = os.path.join(directory, "Zadanie 4." + str(i) + ".py")
    subprocess.call(["python", file])
