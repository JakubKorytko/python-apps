""" Commands handler for neon task """

alph = ['A','B','C','D',
        'E','F','G','H',
        'I','J','K','L',
        'M','N','O','P',
        'Q','R','S','T',
        'U','V','W','X',
        'Y','Z']

def handle(text, command_line):
    """ Handles commands based on given text. """

    [command, arg] = command_line.split(" ")

    if command=="ADD":
        text += arg
    elif command == "DELETE":
        text = text[0:len(text) - int(arg)]
    elif command == "CHANGE":
        text = text[0:len(text) - len(arg)]
        text += arg
    elif command == "MOVE":
        ind = alph.index( arg ) + 1
        if ind>=len(alph):
            ind=0
        text = text.replace(arg, alph[ind], 1)
    return text

def process_commands(data):
    """ Process all commands and returns the final text. """

    result = ""

    for command in data:
        result = handle(result, command.strip())

    return result
