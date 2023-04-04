import os

dir = os.path.dirname(__file__)
file = os.path.join(dir, "anagram.py")
data = open(file).read()
exec(data)