""" Run all tasks from zadania_maturalne[C]/kryptogramy[P] in subprocesses. """

import os
import subprocess

directory = os.path.dirname(__file__)

for i in range(1, 4):
    file = os.path.join(directory, "Zadanie " + str(i) + ".py")
    subprocess.call(["python", file])

    print("\n---\n")
    