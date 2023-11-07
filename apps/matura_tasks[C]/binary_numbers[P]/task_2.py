""" A module that counts numbers divisible by 2 or 8 from a file with binary numbers. """

from os import path as os_path


def count_lines_divisible_by_2_or_8():
    """Returns number of lines in file 'numbers.txt' that are divisible by 2 and 8."""

    numbers_path = os_path.join(os_path.dirname(__file__), "numbers.txt")

    with open(numbers_path, "r", encoding="utf-8") as file:
        count_divisible_by_2 = 0
        count_divisible_by_8 = 0
        for line in file:
            number = int(line, 2)
            if number % 2 == 0:
                count_divisible_by_2 += 1
            if number % 8 == 0:
                count_divisible_by_8 += 1

    return [count_divisible_by_2, count_divisible_by_8]


[DIVISIBLE_BY_2, DIVISIBLE_BY_8] = count_lines_divisible_by_2_or_8()

print("Task 2:\n")
print(f"{DIVISIBLE_BY_2} numbers divisible by 2")
print(f"{DIVISIBLE_BY_8} numbers divisible by 8\n")
