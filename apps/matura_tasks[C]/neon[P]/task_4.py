""" Module that prints the final text from a file with commands. """

from data.commands_handler import process_commands
from data.file_handler import data

FINAL_TEXT = process_commands(data())

print("Task 4:", FINAL_TEXT)
