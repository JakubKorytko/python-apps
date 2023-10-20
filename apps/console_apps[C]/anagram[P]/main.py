""" Runs anagram.py in a subprocess. """

import os
import subprocess

directory = os.path.dirname(__file__)
file = os.path.join(directory, "anagram.py")
subprocess.call(["python", file])
