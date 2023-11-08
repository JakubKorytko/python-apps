""" Decrypts given text using Cezar cipher. """

from data.handler import DIFF, MAX_ORD, MIN_ORD, read_file, save_result


def decrypt(word, k):
    """Decrypts given word using Caesar cipher."""

    result = ""

    for letter in word:
        letter_code = ord(letter)

        if MAX_ORD >= letter_code >= MIN_ORD:
            letter_code -= k % DIFF

            if letter_code < MIN_ORD:
                letter_code = MAX_ORD - (MIN_ORD % letter_code) + 1

            result += chr(letter_code)

    return result


def decrypt_text_from_file_2():
    """Decrypts text from file 2."""

    decrypted_text = ""

    words_file = read_file(2)

    for word in words_file:
        [word, key] = word.split(" ")
        key = key.replace("\n", "")

        key = 0 if key == "" else int(key)

        decrypted_text += decrypt(word, key) + "\n"

    return decrypted_text


def write_decrypted_text_to_file_2(text):
    """Writes decrypted text to file 2."""

    save_result(2, text)


DECRYPTED_TEXT = decrypt_text_from_file_2()
write_decrypted_text_to_file_2(DECRYPTED_TEXT)
