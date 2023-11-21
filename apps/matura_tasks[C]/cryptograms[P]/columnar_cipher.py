""" Functions for decrypting code using columnar cipher. """

import math


def key_to_int_list(key_string):
    """Converts list of chars/strings to list of integers."""

    key_list = key_string.split(",")
    key_int_list = []

    for key in key_list:
        key_int_list.append(int(key))

    return key_int_list


def split_into_columns(code, lengths, columns_number):
    """Splits code into columns."""

    columns = []

    for _ in range(0, columns_number):
        columns.append([])

    for index in range(0, columns_number):
        for _ in range(0, lengths[index]):
            columns[index].append(code[0])
            code = code[1:]

    return columns


def read_letters_in_proper_order(columns, key_to_indices):
    """Reads letters in proper order."""

    result = []

    while sum(len(letter) for letter in columns) > 0:
        for index in range(0, len(columns)):
            i = key_to_indices[index]
            if len(columns[i]) > 0:
                result.append(columns[i].pop(0))

    return "".join(result)


def generate_column_lengths(code_length, columns_number, columns_indices):
    """Generates lengths of columns list."""

    rest = 0

    lengths = []

    for _ in range(0, columns_number):
        lengths.append(math.floor(code_length / columns_number))

    rest = code_length - sum(lengths)

    i = 0
    while rest > 0:
        lengths[columns_indices[i]] += 1
        rest -= 1
        i += 1

    return lengths


def narrow_key_to_indices(key_list):
    """Narrows key to indices."""

    key_to_indices = key_list

    while min(key_to_indices) > 0:
        for i in enumerate(key_to_indices):
            key_to_indices[i] -= 1

    return key_to_indices


def decrypt_code(code, columns_number, key):
    """Decrypts code."""
    code_length = len(code)

    key_list = key_to_int_list(key)

    columns_indices = narrow_key_to_indices(key_list)

    lengths = generate_column_lengths(code_length, columns_number, columns_indices)

    columns = split_into_columns(code, lengths, columns_number)

    result = read_letters_in_proper_order(columns, columns_indices)

    return result
