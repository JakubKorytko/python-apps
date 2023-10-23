""" Encrypts given text using Caesar cipher. """

from data import *

K=107
res = ""

def encrypt(word,k):
    """ Encrypts given word using Caesar cipher. """

    result = ""

    for letter in word:
        letterCode = ord(letter)
        
        if (letterCode>=MIN and letterCode<=MAX):
            letterCode+=(k%DIFF)
            
            if (letterCode>MAX):
                letterCode=MIN+(letterCode%MAX)-1
            
            result+=chr(letterCode)

    return result

wordsFile = readFile("1")

for word in wordsFile:
    res+=encrypt(word, K)+"\n"

wordsFile.close()

resultFile = saveResult("1")
resultFile.truncate(0)
resultFile.write(res)
resultFile.close()
