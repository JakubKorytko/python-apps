import os

dir = os.path.dirname(__file__)
file = os.path.join(dir, "sortLetters.py")
data = open(file).read()
exec(data)