""" Program that checks if a phrase is a palindrome """

from re import IGNORECASE
from re import sub as re_sub


def is_palindrome(phrase):
    """Checks if a phrase is a palindrome"""

    clear_phrase = re_sub(r"[^A-Z0-9]", "", phrase, flags=IGNORECASE)

    left_loop = 0
    right_loop = len(clear_phrase) - 1

    while left_loop <= right_loop:
        if clear_phrase[left_loop] == clear_phrase[right_loop]:
            left_loop += 1
            right_loop -= 1
        else:
            return False

    return True


print("\nThis program checks if a phrase is a palindrome!")
print("(its case insensitive and any spaces or special characters will be removed)\n")
print(
    "Palindrome: a word, phrase, or sequence that reads the same backward as forward,",
    end=" ",
)
print("e.g., sir i demand i am a maid named iris\n")

PHRASE = input("Enter a phrase: ").lower()

if is_palindrome(PHRASE):
    print("It is a palindrome")
else:
    print("It is not a palindrome")
