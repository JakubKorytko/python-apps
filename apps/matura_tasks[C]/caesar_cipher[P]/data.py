""" A module for reading and saving data. """

import os

MIN=65
MAX=90
DIFF=MAX-MIN+1

script_dir = os.path.dirname(__file__)

def readFile(number):
    """ Reads data from a file. """

    txt_path = "data/data_"+number+".txt"
    file = os.path.join(script_dir, txt_path)
    data = open(file)
    return data

def saveResult(number):
    """ Saves result to a file. """

    txt_path = "results/results_"+number+".txt"
    file = os.path.join(script_dir, txt_path)
    data = open(file, "w")
    return data
