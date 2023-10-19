""" App that encrypts a message using columnar transposition cipher. """

import math

print("-Zadanie 2-\n")

print("Format wprowadzonych danych:\n")
print("Kod: lancuch tekstowy (np. AWYKWIAPCSSOYERAZTZCZ)")
print("Liczba kolumn: liczba calkowita (np. 3)")
print("Klucz: ciag liczb calkowitych oddzielonych przecinkami (np. 2,0,1)")
print("Program nie sprawdza poprawnosci wprowadzonych danych.\n")

kod = str(input("Podaj zaszyfrowany kod: "))
l_kolumn = int(input("Podaj liczbe kolumn: "))
klucz = str(input("Podaj klucz (po przecinkach): "))

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

print("\nZaszyfrowane:", kod)

print("Odszyfrowane:",''.join(result))