import os

MIN=65
MAX=90
DIFF=MAX-MIN+1

script_dir = os.path.dirname(__file__)

def readFile(number):
    txt_path = "dane/dane_6_"+number+".txt"
    file = os.path.join(script_dir, txt_path)
    data = open(file)
    return data

def saveResult(number):
    txt_path = "wyniki/wyniki_6_"+number+".txt"
    file = os.path.join(script_dir, txt_path)
    data = open(file, "w")
    return data