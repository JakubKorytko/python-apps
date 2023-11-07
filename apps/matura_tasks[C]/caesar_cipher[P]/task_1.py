""" Encrypts given text using Caesar cipher. """

from data.handler import MIN_ORD, MAX_ORD, DIFF, read_file, save_result

K = 107


def encrypt(word, k):
    """Encrypts given word using Caesar cipher."""

    result = ""

    for letter in word:
        letter_code = ord(letter)

        if MAX_ORD >= letter_code >= MIN_ORD:
            letter_code += k % DIFF

            if letter_code > MAX_ORD:
                letter_code = MIN_ORD + (letter_code % MAX_ORD) - 1

            result += chr(letter_code)

    return result


def encrypt_text_from_file_1():
    """Encrypts text from file 1."""

    encrypted_text = ""

    words_file = read_file(1)

    for word in words_file:
        encrypted_text += encrypt(word, K) + "\n"

    return encrypted_text


def write_encrypted_text_to_file_1(text):
    """Writes encrypted text to file 1."""

    save_result(1, text)


ENCRYPTED_TEXT = encrypt_text_from_file_1()
write_encrypted_text_to_file_1(ENCRYPTED_TEXT)
