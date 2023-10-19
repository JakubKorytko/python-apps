""" App that calculate string length after performing a series of operations from a file with commands """

from data import data
from handle import handle

text = ""

for command in data():
    text = handle(text, command.strip())

print("Zadanie 4.1:", len(text))
