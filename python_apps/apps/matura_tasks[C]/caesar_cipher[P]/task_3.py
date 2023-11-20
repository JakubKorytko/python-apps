""" A module that finds words that are incorrectly encrypted with the Caesar cipher from a file. """

from data.handler import MAX_ORD, MIN_ORD, read_file, save_result


def decrypt(word, encrypted):
    """Decrypts given word using Caesar cipher."""

    res = ""
    elements = []
    for index, letter in enumerate(word):
        code = ord(letter)
        encrypted_code = ord(encrypted[index])

        val = (
            MAX_ORD - code + encrypted_code - MIN_ORD + 1
            if (code > encrypted_code)
            else encrypted_code - code
        )

        elements.append(val)

    res = all(el == elements[0] for el in elements)

    return word if not res else False


def find_incorrectly_encrypted_words_in_file_3():
    """Finds incorrectly encrypted words."""

    incorrectly_encrypted_words = ""

    words_file = read_file(3)

    for word in words_file:
        both_versions = word.split(" ")

        both_versions[1] = both_versions[1].replace("\n", "")

        decrypted = decrypt(*both_versions)

        if decrypted:
            incorrectly_encrypted_words += decrypted + "\n"

    return incorrectly_encrypted_words


def write_incorrectly_encrypted_words_to_file_3(text):
    """Saves incorrectly encrypted words to a file."""

    save_result(3, text)


INCORRECTLY_ENCRYPTED_WORDS_STRING = find_incorrectly_encrypted_words_in_file_3()
write_incorrectly_encrypted_words_to_file_3(INCORRECTLY_ENCRYPTED_WORDS_STRING)
