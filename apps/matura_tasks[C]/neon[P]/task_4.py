""" A app that prints the final text from a file with commands. """

from data.file_handler import data
from data.commands_handler import handle

def process_commands_from_file():
    """ Process commands from file. """

    result = ""

    for command in data():
        result = handle(result, command.strip())

    return result

FINAL_TEXT = process_commands_from_file()

print("Task 4:", FINAL_TEXT)
