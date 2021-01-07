"""
Write a Python program to convert JSON data to Python object
It mustn't give errors
"""

import json
import os

json_dir = 'testjson.json'
data = []

while True:
    print("would you like to use the default file? (y/n)")
    def_or_input = input()
    if def_or_input != 'y' and def_or_input != 'n':
        print("Not acceptable answer.")
    else:
        break

if def_or_input == 'n':
    while True:
        print("type in directory:")
        dir_of_json = input()
        if os.path.exists(dir_of_json):
            json_dir = dir_of_json
            break
        else:
            print('type in valid dir')

with open(json_dir, "r") as json_open:
    data = json.load(json_open)

print(data)