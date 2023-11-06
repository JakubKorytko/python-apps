""" App that decrypts a message using columnar transposition cipher. """

from columnar_cipher import decrypt_code

print("-Task 2-\n")

print("Format of input data:\n")
print("Code: string (e.g. 'LYRNAOHDCPUAS')")
print("Number of columns: integer (e.g. 3)")
print("Key: list of integers separated by commas (e.g. 2,0,1)\n")
print("Program does not check correctness of input data.\n")

CODE = str(input("Enter encoded message: "))
COLUMNS_NUMBER = int(input("Enter number of columns: "))
KEY = str(input("Enter key (separated by commas): "))

print("\nEncrypted:", CODE)

print("Decrypted:", decrypt_code(CODE, COLUMNS_NUMBER, KEY))
