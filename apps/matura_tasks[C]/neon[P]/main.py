""" Runs all tasks from matura_tasks[C]/neon[P] in subprocesses. """

import os
import subprocess

directory = os.path.dirname(__file__)

for i in range(1, 5):
    file = os.path.join(directory, "task_" + str(i) + ".py")
    subprocess.call(["python", file])
