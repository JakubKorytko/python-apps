""" This program will find anagrams in a list of words """

print("This program will find anagrams in a list of words\n")


def ordinal(number):
    """Returns ordinal number of a number"""

    if 10 <= number % 100 < 20:
        return str(number) + "th"

    return str(number) + {1: "st", 2: "nd", 3: "rd"}.get(number % 10, "th")


def present(anagrams, *args):
    """Returns True if anagram is in the list"""

    arr = sorted([*args])
    for anagram in anagrams:
        if anagram == arr:
            return True

    return False


def read_words():
    """Reads words from the user input and returns them in a list,
    also returns a list of sorted letters in each word"""

    words = []
    sorted_letters = []

    i = 1

    while True:
        word = input(
            f"Enter the {ordinal(i)} word: (leave empty field to end the input) "
        )

        if word == "":
            break

        letters = list(word)
        words.append(word)
        sorted_letters.append(sorted(letters))
        i += 1

    return words, sorted_letters


def get_anagrams(words, sorted_letters):
    """Returns anagrams from the list of words and sorted letters"""

    anagrams = []

    for index_1, letters_list_1 in enumerate(sorted_letters):
        for index_2, letters_list_2 in enumerate(sorted_letters):
            words_pair = [words[index_1], words[index_2]]

            if (
                letters_list_1 == letters_list_2
                and words_pair[0] != words_pair[1]
                and not present(anagrams, *words_pair)
            ):
                anagrams.append(sorted(words_pair))

    return anagrams


[WORDS, SORTED_LETTERS] = read_words()
ANAGRAMS = get_anagrams(WORDS, SORTED_LETTERS)

if len(ANAGRAMS) == 0:
    print("\nThere are no anagrams in the list")

else:
    print("\nWords", *ANAGRAMS, "are anagrams")
