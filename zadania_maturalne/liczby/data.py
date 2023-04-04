import os

script_dir = os.path.dirname(__file__)
txt_path = "liczby.txt"
file = os.path.join(script_dir, txt_path)

numbers = open(file)