""" App that counts numbers that have more zeros than ones in a file with binary numbers. """

from data import numbers

amount = 0

for number in numbers():
    zerosAndOnes = [0, 0]
    
    for digit in number:
        if (digit.isnumeric()):
            zerosAndOnes[int(digit)]+=1
    if (zerosAndOnes[0]>zerosAndOnes[1]):
        amount+=1

print("Zad 4.1:", amount)
