""" A module that finds the smallest and largest number from a file with binary numbers. """

from os import path as os_path


def find_lines_with_smallest_and_largest_numbers():
    """Returns the lines in file 'numbers.txt' that have the smallest and the biggest number."""

    min_index = -1
    max_index = -1

    numbers_path = os_path.join(os_path.dirname(__file__), "numbers.txt")

    with open(numbers_path, "r", encoding="utf-8") as file:
        numbers = []
        for line in file:
            numbers.append(int(line, 2))

        min_index = numbers.index(min(numbers)) + 1
        max_index = numbers.index(max(numbers)) + 1

    return [min_index, max_index]


[
    SMALLEST_NUMBER_LINE,
    LARGEST_NUMBER_LINE,
] = find_lines_with_smallest_and_largest_numbers()

print("Task 3:\n")
print(f"the smallest number is in the line {SMALLEST_NUMBER_LINE}")
print(f"the largest number is in the line {LARGEST_NUMBER_LINE}\n")
