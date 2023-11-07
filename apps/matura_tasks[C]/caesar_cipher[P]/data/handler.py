""" A module for reading and saving data. """

import os

MIN_ORD = 65
MAX_ORD = 90
DIFF = MAX_ORD - MIN_ORD + 1

script_dir = os.path.dirname(__file__)


def read_file(number):
    """Reads data from a file."""

    txt_path = f"source/data_{number}.txt"
    file = os.path.join(script_dir, txt_path)
    with open(file, "r", encoding="utf-8") as data:
        return data.readlines()


def save_result(number, data):
    """Saves result to a file."""

    txt_path = f"results/results_{number}.txt"
    file = os.path.join(script_dir, txt_path)
    with open(file, "w", encoding="utf-8") as result_file:
        result_file.truncate(0)
        result_file.write(data)
