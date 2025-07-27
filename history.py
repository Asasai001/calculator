import json
import os


def history_save(operations):
    with open('calculator_history.json', 'w') as file:
        json.dump(operations, file, indent=4)


def history_load():
    if not os.path.exists('calculator_history.json'):
        return []
    try:
        with open('calculator_history.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return f'File {file} not found'