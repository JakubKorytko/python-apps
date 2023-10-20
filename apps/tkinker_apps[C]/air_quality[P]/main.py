""" Runs air_quality.py in a subprocess. """

import os
import subprocess

directory = os.path.dirname(__file__)
file = os.path.join(directory, "air_quality.py")
subprocess.call(["python", file])
