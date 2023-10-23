""" Module for loading data from file. """

import os

script_dir = os.path.dirname(__file__)

def numbers():
    """ Returns file object with numbers. """

    txt_path = "numbers.txt"
    file = os.path.join(script_dir, txt_path)

    return open(file)
