import json
import os

def load_game():
    saves_file = os.path.join(os.path.dirname(__file__), 'saves.JSON')
    with open(saves_file, 'r') as f:
        return json.load(f)

def save_game(data):
    saves_file = os.path.join(os.path.dirname(__file__), 'saves.JSON')
    with open(saves_file, 'w') as f:
        json.dump(data, f)