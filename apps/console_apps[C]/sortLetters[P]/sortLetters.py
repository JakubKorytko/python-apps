""" A program that sorts letters in a word or phrase. """

def clear(text):
    """ Clears text from spaces and punctuation. """

    replacements = [" ", ",", ".", "!", "?", ":", ";", "'", '"', "(", ")", "[", "]", "{", "}", "/", "\\", "|", "_", "-", "+", "=", "*", "&", "^", "%", "$", "#", "@", "~", "`"]
    for replacement in replacements:
        text = text.replace(replacement, "")
    return text


print("\nWelcome to the Letter Sorter App!")
print("Enter a word or phrase and I will sort the letters for you.")
print("Keep in mind that the final output will be in lower case, without spaces and punctuation.")

text = input("\nEnter a word or phrase: ")

def split(word): 
    """ Splits a word into a list of letters. """

    return [char for char in word]

text = clear(text).lower()

# print(text)

words = split(text)

words.sort()

# print(words)


print_string = "\nHere are the sorted letters in your word or phrase: "

i = 0
for word in words:
    # print(word+"\n")
    if i==len(words)-1:
        print_string +=word
    else:
        print_string += word+","
    i+=1

print(print_string)
