""" A module that counts the most frequently added character from a file of commands. """

from data.file_handler import data


def get_letters_occurences():
    """Returns a dictionary with added letters occurences."""

    occurences = {}

    for command_line in data():
        [command, arg] = command_line.strip().split(" ")

        if command != "ADD":
            continue

        if occurences.get(arg) is None:
            occurences[arg] = 0

        occurences[arg] += 1

    return occurences


LETTERS_OCCURENCES = get_letters_occurences()
MOST_FREQUENTLY_ADDED_LETTER = max(LETTERS_OCCURENCES, key=LETTERS_OCCURENCES.get)
MOST_FREQUENTLY_ADDED_LETTER_COUNT = LETTERS_OCCURENCES[MOST_FREQUENTLY_ADDED_LETTER]

print("Task 3:", MOST_FREQUENTLY_ADDED_LETTER, MOST_FREQUENTLY_ADDED_LETTER_COUNT)
