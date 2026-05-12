import json
def load_game():
    with open('saves.JSON', 'r') as f:
        return(json.load(f))
def save_game(data):
    with open('saves.JSON', 'w') as f:
        json.dump(data, f)