import os

dir = os.path.dirname(__file__)
file = os.path.join(dir, "palindrome.py")
data = open(file).read()
exec(data)