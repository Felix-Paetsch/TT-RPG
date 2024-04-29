import json

def load_obj(filename):
    with open(filename, 'r') as file:
        return json.load(file)
