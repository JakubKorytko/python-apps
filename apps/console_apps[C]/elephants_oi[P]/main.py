""" Runs elephants.py in a subprocess. """

import os
import subprocess

directory = os.path.dirname(__file__)
file = os.path.join(directory, "elephants.py")
subprocess.call(["python", file])
