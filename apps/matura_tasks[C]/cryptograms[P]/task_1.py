""" App that decrypts a hardcoded message using columnar transposition cipher. """

import math

def key_to_int_list(key):
    """ Converts list of strings to list of integers. """

    key_list = key.split(",")
    key_int_list = []

    for key in key_list:
        key_int_list.append(int(key))

    return key_int_list

def split_into_columns(code, lengths, columns_number):
    """ Splits code into columns. """

    columns = []

    for _ in range(0, columns_number):
        columns.append([])

    for x in range(0, columns_number):
        for _ in range(0, lengths[x]):
            columns[x].append(code[0])
            code = code[1:]

    return columns

def read_letters_in_proper_order(columns, key_to_indices):
    """ Reads letters in proper order. """

    result = []

    while sum(len(x) for x in columns) > 0:
        for x in range(0, len(columns)):
            i = key_to_indices[x]
            if len(columns[i]) > 0:
                result.append(columns[i].pop(0))

    return ''.join(result)

def generate_column_lengths(code_length, columns_number, columns_indices):
    """ Generates lengths of columns list. """

    rest = 0

    lengths = []

    for _ in range(0, columns_number):
        lengths.append(math.floor(code_length/columns_number))

    rest = code_length - sum(lengths)

    i = 0
    while rest > 0:
        lengths[columns_indices[i]] += 1
        rest -= 1
        i += 1

    return lengths

def narrow_key_to_indices(key_list):
    """ Narrows key to indices. """

    key_to_indices = key_list

    while min(key_to_indices) > 0:
        for i in enumerate(key_to_indices):
            key_to_indices[i] -= 1

    return key_to_indices

print("-Task 1-\n")

CODE = "LYRNAOHDCPUAS"
COLUMNS_NUMBER = 3
KEY = "2,0,1"

CODE_LENGTH = len(CODE)

KEY_LIST = key_to_int_list(KEY)

COLUMNS_INDICES = narrow_key_to_indices(KEY_LIST)

LENGTHS = generate_column_lengths(CODE_LENGTH, COLUMNS_NUMBER, COLUMNS_INDICES)

COLUMNS = split_into_columns(CODE, LENGTHS, COLUMNS_NUMBER)

RESULT = read_letters_in_proper_order(COLUMNS, COLUMNS_INDICES)

print("Encrypted:", CODE)

print("Decrypted:", RESULT)
