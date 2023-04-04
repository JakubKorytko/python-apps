print("This program will find anagrams in a list of words\n")

i=1
words = []
sortedLetters = []
anagrams = []
word="start"

def ordinal(n):
    if 10 <= n % 100 < 20:
        return str(n) + 'th'
    else:
        return str(n) + {1 : 'st', 2 : 'nd', 3 : 'rd'}.get(n % 10, "th")

def present(*args):
    arr = sorted([*args])
    for el in anagrams:
        if el == arr: return True
    return False

while (True):
    word = input("Enter the {0} word: (leave empty field to end the input) ".format(ordinal(i)))
    if word == "": break

    letters = [char for char in word] 
    words.append(word)
    sortedLetters.append(sorted(letters))
    i+=1
    

for index_1, el_1 in enumerate(sortedLetters):
    for index_2, el_2 in enumerate(sortedLetters):
        tabs = [words[index_1], words[index_2]]
        if el_1==el_2 and tabs[0]!=tabs[1] and not present(*tabs):
            anagrams.append(sorted(tabs))

if len(anagrams) == 0: print("\nThere are no anagrams in the list")
else: print("\nWords",*anagrams,"are anagrams")
    