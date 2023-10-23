""" A module that counts numbers divisible by 2 and 8 from a file with binary numbers. """

from data import numbers

divisibleBy2 = 0
divisibleBy8 = 0

for number in numbers():
    if (int(number,2)%2==0): divisibleBy2+=1
    if (int(number,2)%8==0): divisibleBy8+=1

print("Task 2:\ndivisible by 2:", divisibleBy2, "\ndivisible by 8:", divisibleBy8)
