""" A app that prints the final text from a file with commands. """

from data import data
from handle import handle

text = ""

for command in data():
    text = handle(text, command.strip())

print("Task 4:", text)
