""" A module that finds words that are incorrectly encrypted with the Caesar cipher from a file. """

from data import *

res = ""

def decrypt(word, encrypted):
    """ Decrypts given word using Caesar cipher. """

    res = ""
    elements = []
    for index, letter in enumerate(word):
        code = ord(letter)
        encCode = ord(encrypted[index])

        val = MAX-code + encCode-MIN + 1 if (code>encCode) else encCode-code
        elements.append(val)
    
    res = all(el == elements[0] for el in elements)

    return word if not res else False

wordsFile = readFile("3")

for word in wordsFile:

    bothVersions = word.split(" ")
    
    bothVersions[1] = bothVersions[1].replace("\n", "")

    decrypted = decrypt(*bothVersions)

    if (decrypted != False): res+=decrypted+"\n"

wordsFile.close()

resultFile = saveResult("3")
resultFile.truncate(0)
resultFile.write(res)
resultFile.close()
