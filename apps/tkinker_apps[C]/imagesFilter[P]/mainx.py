""" Runs imagesFilter.py in a subprocess. """

import os
import subprocess

dir = os.path.dirname(__file__)
file = os.path.join(dir, "imagesFilter.py")
subprocess.call(["python", file])
