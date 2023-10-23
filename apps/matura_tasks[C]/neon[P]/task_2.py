""" A module that counts the longest sequence of the same command from a file with commands. """

from data import data

count = {
    "ADD":0,
    "MOVE":0,
    "DELETE":0,
    "CHANGE":0,
    "INIT":0
}

instruction="INIT"
index=0

for command in data():
    commandArray = command.strip().split(" ")
    if (instruction!=commandArray[0]):
        if (index>count[instruction]):
            count[instruction]=index
        index=0
    instruction=commandArray[0]
    index+=1

maxName = max(count, key=count.get)
maxVal = count[maxName]

print("Task 2:",maxName,maxVal)
