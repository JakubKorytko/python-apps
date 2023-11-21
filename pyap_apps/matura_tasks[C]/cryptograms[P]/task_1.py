""" App that decrypts a hardcoded message using columnar transposition cipher. """

from columnar_cipher import decrypt_code

print("-Task 1-\n")

CODE = "LYRNAOHDCPUAS"
COLUMNS_NUMBER = 3
KEY = "2,0,1"

print("Encrypted:", CODE)

print("Decrypted:", decrypt_code(CODE, COLUMNS_NUMBER, KEY))
