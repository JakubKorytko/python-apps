""" App that decrypts a message using columnar transposition cipher. """

import math

print("-Zadanie 1-\n")

kod = "AWYKWIAPCSSOYERAZTZCZ"
l_kolumn =  3
klucz = "2,0,1"

dl_kodu = len(kod)
klucz = klucz.split(",")
times = math.ceil(dl_kodu/l_kolumn)
numbers = [0]*dl_kodu
kod2 = list(kod)
result = [""]*dl_kodu

for x in range(0, dl_kodu):
    numbers[int(x/l_kolumn)]+=1

for m in range(0, len(klucz)*times):
    l = int(m/times)
    k = int(klucz[l])
    mod = m%times

    if numbers[mod]>k: result[mod*l_kolumn+k] = kod2.pop(0)

print("Zaszyfrowane:", kod)

print("Odszyfrowane:",''.join(result))
