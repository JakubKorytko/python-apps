import os

script_dir = os.path.dirname(__file__)

def numbers():
    txt_path = "liczby.txt"
    file = os.path.join(script_dir, txt_path)

    return open(file)