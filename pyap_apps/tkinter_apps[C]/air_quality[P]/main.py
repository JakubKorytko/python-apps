""" Runs air_quality.py in a subprocess. """

import os
import subprocess
from sys import executable

PYTHON = executable or "python"

directory = os.path.dirname(__file__)
file = os.path.join(directory, "air_quality.py")
subprocess.call([PYTHON, file])
