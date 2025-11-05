import json
import os

def load_config():
    config_path = os.path.join(os.path.dirname(__file__),"..","data","testdata.json")
    with open(config_path, "r") as file:
        return json.load(file)
