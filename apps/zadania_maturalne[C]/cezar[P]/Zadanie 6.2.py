from data import *

res = ""

def decrypt(word,k):
    
    result = ""
    
    for letter in word:
        
        letterCode = ord(letter)
        
        if (letterCode>=MIN and letterCode<=MAX):
            letterCode-=(k%DIFF)

            if (letterCode<MIN):
                letterCode=MAX-(MIN%letterCode)+1
            
            result+=chr(letterCode)

    return result

wordsFile = readFile("2")

for word in wordsFile:
    
    wordAndKey = word.split(" ")
    wordAndKey[1] = wordAndKey[1].replace("\n", "")

    wordAndKey[1] = 0 if wordAndKey[1] == '' else int(wordAndKey[1])
    
    res+=decrypt(*wordAndKey)+"\n"

wordsFile.close()

resultFile = saveResult("2")
resultFile.truncate(0)
resultFile.write(res)
resultFile.close()