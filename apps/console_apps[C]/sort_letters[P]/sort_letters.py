""" A program that sorts letters in a word or phrase. """

def clear(text):
    """ Clears text from spaces and punctuation. """

    replacements = [" ", ",", ".", "!", "?", ":", ";", "'", '"', "(", ")",
    "[", "]", "{", "}", "/", "\\", "|", "_", "-", "+", "=", "*", "&", "^",
    "%", "$", "#", "@", "~", "`"]

    for replacement in replacements:
        text = text.replace(replacement, "")
    return text

def split(word):
    """ Splits a word into a list of letters. """

    return list(word)

def get_input():
    """ Gets input from the user and clears it. """

    text = input("\nEnter a word or phrase: ")
    text = clear(text).lower()

    return text

def split_and_sort(text):
    """ Splits text into a list of letters and sorts them. """

    letters = split(text)
    letters.sort()

    return letters

PRINT_STRING = "\nHere are the sorted letters in your word or phrase: "

print("\nWelcome to the Letter Sorter App!")
print("Enter a word or phrase and I will sort the letters for you.")
print("Keep in mind that the final output will be in lower case, without spaces and punctuation.")

TEXT = get_input()
LETTERS = split_and_sort(TEXT)

i = 0
for letter in LETTERS:

    if i==len(LETTERS)-1:
        PRINT_STRING += letter
    else:
        PRINT_STRING += letter + ","

    i+=1

print(PRINT_STRING)
