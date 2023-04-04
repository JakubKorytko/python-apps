from data import numbers

divisibleBy2 = 0 #liczby podzielne przez 2
divisibleBy8 = 0 #liczby podzielne przez 8

for number in numbers:
    if (int(number,2)%2==0): divisibleBy2+=1
    if (int(number,2)%8==0): divisibleBy8+=1

print("Zad 4.2: podzielne przez 2:",divisibleBy2,"\npodzielne przez 8:",divisibleBy8)
