""" Runs anagram.py in a subprocess. """

import os
import subprocess

dir = os.path.dirname(__file__)
file = os.path.join(dir, "anagram.py")
subprocess.call(["python", file])
