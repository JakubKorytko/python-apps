print("-Zadanie 3-\n")

text = "WLASNE MALE OGNISKO CENNIEJSZE OD STOSU ZLOTA"

print("Odszyfrowane:",text)

table = [[], []]
letters=0
for letter in text:
    if letter!=" ":
        letters+=1
        table[1-(letters%2)].append(letter)
            
str = ''.join(table[0]) + ''.join(table[1])

print("Zaszyfrowane:",str)