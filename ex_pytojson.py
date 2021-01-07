"""
Python JSON: Convert Python object to JSON data
"""
import json

python_object = {
    "balls": "2",
    "muscles": "9001",
    "date": "9/11",
    "street": "Sesame street",
}

with open("dumpfile.json", "w") as write_file:
    json.dump(python_object, write_file)