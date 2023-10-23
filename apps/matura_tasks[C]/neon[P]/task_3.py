""" A module that counts the most common letter from a file with commands. """

from data import data
from handle import handle, alph

count = dict.fromkeys(alph, 0)
text = ""

for command in data():
    command_stripped = command.strip()
    commandArray = command_stripped.split(" ")
    if (commandArray[0]=="ADD"):
        count[commandArray[1]] += 1
    text = handle(text, command_stripped)

max_count = max(count)

print("Task 3:",max_count,count[max_count])
