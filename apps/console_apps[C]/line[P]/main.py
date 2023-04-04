import os

dir = os.path.dirname(__file__)
file = os.path.join(dir, "line.py")
data = open(file).read()
exec(data)