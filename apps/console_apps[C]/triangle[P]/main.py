import os
import subprocess

dir = os.path.dirname(__file__)
file = os.path.join(dir, "triangle.py")
subprocess.call(["python", file])