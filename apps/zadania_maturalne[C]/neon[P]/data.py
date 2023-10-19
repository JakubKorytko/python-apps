""" Module for reading data from file. """

import os

script_dir = os.path.dirname(__file__)

def data():
    """ Returns data from file. """

    txt_path = "dane/instrukcje.txt"
    file = os.path.join(script_dir, txt_path)

    return open(file, encoding="utf-8")
