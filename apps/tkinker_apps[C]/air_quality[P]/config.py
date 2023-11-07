""" Configuration file for air_quality.py """

import json
import os

# dropdown? - set this to false in order to open city selection in new window instead of dropdown
# font - set font name and size


def get_config():
    """Returns config from config.json."""

    script_dir = os.path.dirname(__file__)
    txt_path = "config.json"
    file = os.path.join(script_dir, txt_path)

    with open(file, "r", encoding="utf-8") as file:
        return json.load(file)
