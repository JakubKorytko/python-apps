""" A module that finds the smallest and largest number from a file with binary numbers. """

from data import numbers

numbersIn10 = [int(x,2) for x in numbers()]

minNumber = min(numbersIn10)
maxNumber = max(numbersIn10)

minRow = numbersIn10.index(minNumber)+1
maxRow = numbersIn10.index(maxNumber)+1

print("Zad 4.3: wiersz najmniejszej:",minRow,"\nwiersz najwiekszej:",maxRow)
