""" Runs all tasks from zadania_maturalne[C]/liczby[P] in subprocesses. """

import os
import subprocess

directory = os.path.dirname(__file__)

for i in range(1, 4):
    file = os.path.join(directory, "Zadanie 4." + str(i) + ".py")
    subprocess.call(["python", file])
