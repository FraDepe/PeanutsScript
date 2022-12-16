import json
import os

def getPath():
    
    here = os.path.dirname(os.path.abspath(__file__))

    config_path = os.path.join(here, "peanuts_config.json")

    with open(config_path, 'r') as file:
        path = json.load(file)["path"]
    print(path)
    return path

if __name__ == "__main__":
    getPath()