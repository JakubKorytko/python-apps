""" A module that counts the longest sequence of the same command from a file with commands. """

from data.file_handler import data


def get_commands_occurences():
    """Returns a dictionary with commands occurences."""

    occurences = {}
    init = True
    index = 0
    instruction = ""

    for command_line in data():
        [command, _] = command_line.strip().split(" ")

        if init:
            instruction = command
            init = False

        if occurences.get(command) is None:
            occurences[command] = 0

        if instruction != command:
            if index > occurences[instruction]:
                occurences[instruction] = index

            index = 0

        instruction = command
        index += 1

    return occurences


def get_name_and_value_of_command_with_longest_sequence(commands_occurences):
    """Returns a command with the longest sequence of the same command."""

    command_with_longest_sequence = max(
        commands_occurences, key=commands_occurences.get
    )
    longest_sequence = commands_occurences[command_with_longest_sequence]

    return command_with_longest_sequence, longest_sequence


COMMANDS_OCCURENCES = get_commands_occurences()
[
    COMMAND_WITH_LONGEST_SEQUENCE,
    LONGEST_SEQUENCE,
] = get_name_and_value_of_command_with_longest_sequence(COMMANDS_OCCURENCES)

print("Task 2:", COMMAND_WITH_LONGEST_SEQUENCE, LONGEST_SEQUENCE)
