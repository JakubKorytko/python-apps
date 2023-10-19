""" Runs line.py in a subprocess. """

import os
import subprocess

dir = os.path.dirname(__file__)
file = os.path.join(dir, "line.py")
subprocess.call(["python", file])
