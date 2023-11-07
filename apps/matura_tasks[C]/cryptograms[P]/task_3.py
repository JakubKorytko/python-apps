""" App that encrypts a message using rail fence cipher. """


def split_into_fence_of_height_2(text):
    """Splits text into fence of height 2."""

    fence = [[], []]
    letters = 0

    for letter in text:
        if letter != " ":
            letters += 1
            fence[1 - (letters % 2)].append(letter)

    return fence


def fence_of_height_2_to_string(fence):
    """Converts fence to string."""

    return "".join(fence[0]) + "".join(fence[1])


print("-Task 3-\n")

TEXT = "A QUICK BROWN FOX JUMPS OVER THE LAZY DOG"

FENCE = split_into_fence_of_height_2(TEXT)
RESULT = fence_of_height_2_to_string(FENCE)

print("Decrypted:", TEXT)
print("Encrypted:", RESULT)
