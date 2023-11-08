""" App that calculate string length after performing
a series of operations from a file with commands """

from data.commands_handler import process_commands
from data.file_handler import data

FINAL_TEXT = process_commands(data())
FINAL_TEXT_LENGTH = len(FINAL_TEXT)

print("Task 1:", FINAL_TEXT_LENGTH)
