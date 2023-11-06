""" A app that prints the final text from a file with commands. """

from data.file_handler import data
from data.commands_handler import process_commands

FINAL_TEXT = process_commands(data())

print("Task 4:", FINAL_TEXT)
