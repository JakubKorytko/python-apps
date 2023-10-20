""" Configuration file for air_quality.py """

import json
import os

# dropdown? - set this to false in order to open city selection in new window instead of dropdown
# font - set font name and size

script_dir = os.path.dirname(__file__)
txt_path = "config.json"
file = os.path.join(script_dir, txt_path)

file = open(file, "r")
config = json.load(file)
