import json

with open("students.json") as in_file:
    data = json.load(in_file)

print(data['dogs'])