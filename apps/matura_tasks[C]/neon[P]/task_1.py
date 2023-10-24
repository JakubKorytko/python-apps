""" App that calculate string length after performing
a series of operations from a file with commands """

from data.file_handler import data
from data.commands_handler import handle

def process_commands_from_file():
    """ Process commands from file. """

    result = ""

    for command in data():
        result = handle(result, command.strip())

    return result

FINAL_TEXT = process_commands_from_file()
FINAL_TEXT_LENGTH = len(FINAL_TEXT)

print("Task 1:", FINAL_TEXT_LENGTH)
