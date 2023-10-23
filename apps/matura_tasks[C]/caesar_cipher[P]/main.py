""" Run all tasks from matura_tasks[C]/caesar_cipher[P] in subprocesses and save results to files. """

import os
import subprocess

directory = os.path.dirname(__file__)

for i in range(1, 4):
    file = os.path.join(directory, "task_" + str(i) + ".py")
    subprocess.call(["python", file])

print("The results are located in the 'results' folder in the files:", end=" ")
print("'results_1.txt', 'results_2.txt', 'results_3.txt")
