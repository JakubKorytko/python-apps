""" Run all tasks from matura_tasks[C]/cryptograms[P] in subprocesses. """

import os
import subprocess
from sys import executable

PYTHON = executable or "python"

directory = os.path.dirname(__file__)

for i in range(1, 4):
    file = os.path.join(directory, "task_" + str(i) + ".py")
    subprocess.call([PYTHON, file])

    print("\n---\n")
