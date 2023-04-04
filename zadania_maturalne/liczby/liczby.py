#ZADANIE 1
def zad1():
    f = open("liczby.txt", "r")
    z = 0
    for x in f:
        i = [0, 0]
        for y in x:
            if (y.isnumeric()):
                i[int(y)]+=1
        if (i[0]>i[1]):
            z+=1
    return z

#ZADANIE 2
def zad2():
    f = open("liczby.txt", "r")
    z = 0 #liczby podzielne przez 2
    k = 0 #liczby podzielne przez 8
    for x in f:
        if (int(x,2)%2==0):
            z+=1
        if (int(x,2)%8==0):
            k+=1
    return [z,k]

#ZADANIE 3
def zad3():
    f = open("liczby.txt", "r")
    z = []
    for x in f:
        z.append(int(x,2))
    return [z.index(min(z))+1, z.index(max(z))+1]

odp1 = zad1()
odp2 = zad2()
odp3 = zad3()

print(str(odp1)+" liczb ma w swoim zapisie binarnym wiecej zer niz jedynek")
print(str(odp2[0])+" liczb podzielnych przez 2")
print(str(odp2[1])+" liczb podzielnych przez 8")
print("w "+str(odp3[0])+" linijce znajduje sie najmniejsza liczba")
print("w "+str(odp3[1])+" linijce znajduje sie najwieksza liczba")