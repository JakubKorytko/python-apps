print("\nThis program checks if a phrase is a palindrome! (its case insensitive)\n")
print("Palindrome: a word, phrase, or sequence that reads the same backward as forward, e.g., madam or nurses run.\n")

phrase = input("Enter a phrase: ").lower()

isPalindrome=1

leftLoop = 0
rightLoop = len(phrase) - 1

while (leftLoop <= rightLoop): 

    if (phrase[leftLoop] == phrase[rightLoop]): 
        leftLoop += 1
        rightLoop -= 1
    else:
        isPalindrome=0
        break
    
if isPalindrome:
    print("It is a palindrome")
else:
    print("It is not a palindrome")