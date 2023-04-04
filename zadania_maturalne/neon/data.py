import os

script_dir = os.path.dirname(__file__)
txt_path = "dane/instrukcje.txt"
file = os.path.join(script_dir, txt_path)

data = open(file)