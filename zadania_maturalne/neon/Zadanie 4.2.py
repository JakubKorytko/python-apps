from data import data

count = {
    "DOPISZ":0,
    "PRZESUN":0,
    "USUN":0,
    "ZMIEN":0,
    "ROZRUCH":0
}

instruction="ROZRUCH"
index=0

for command in data:
    commandArray = command.strip().split(" ")
    if (instruction!=commandArray[0]):
        if (index>count[instruction]):
            count[instruction]=index
        index=0
    instruction=commandArray[0]
    index+=1

maxName = max(count)
maxVal = count[maxName]

print("Zadanie 4.2:",maxName,maxVal)
