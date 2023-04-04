from data import data
from handle import handle

text = ""

for command in data():
    text = handle(text, command.strip())

print("Zadanie 4.4:", text)
