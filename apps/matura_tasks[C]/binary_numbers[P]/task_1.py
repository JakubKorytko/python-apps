""" App that counts numbers that have more zeros than ones in a file with binary numbers. """

def numbers_with_more_zeros_than_ones():
    """ Returns number of lines in file 'numbers.txt' that have more zeros than ones. """

    numbers_with_more_zeros = 0

    with open("numbers.txt", "r", encoding="utf-8") as file:
        for line in file:
            count = [0, 0]
            for char in line:
                if char.isnumeric():
                    count[int(char)] += 1
            if count[0] > count[1]:
                numbers_with_more_zeros += 1

        return numbers_with_more_zeros

print("Task 1:\n")
print(
    numbers_with_more_zeros_than_ones(),
    "numbers have more zeros than ones in their binary notation\n"
)
