# import pickle
#
# data = {
#     'a': [1, 2.0, 3, 4 + 6j],
#     'b': ("Alice has a cat", "Python programming is great"),
#     'c': [False, True, False]
# }
#
# with open('data.pickle', 'wb') as f:
#     pickle.dump(data, f)
#
# with open('data.pickle', 'rb') as f:
#     print(pickle.load(f))
#
# import csv
#
# with open("employees.csv", 'a', newline='') as out_file:
#     writer = csv.writer(out_file)
#     writer.writerow(["Anna", 2500])
#
# with open("employees.csv") as in_file:
#     reader = csv.reader(in_file)
#     for row in reader:
#         print(row)

import json

animals = {
    "dogs": [{
        "id": 0,
        "name": "maja",
        "race": "dog"
    }, {
        "id": 1,
        "name": "asvasv",
        "race": "dog"
    }],
    "cats": [{
        "id": 0,
        "name": "btsdb",
        "race": "cat"
    }, {
        "id": 1,
        "name": "btsbdt",
        "race": "cat"
    }]
}

data = {"mouse": [{
    "id": 0,
    "name": "btsbdt",
    "race": "mouse"
}]}

newel = {"mices": [{
        "id": 0,
        "name": "liulek",
        "racce": "moouse",
    }, {
        "id": 1,
        "name": "Jerry",
        "racce": "moouse",
    }]
}

with open("animals.json", 'r') as read_file:
    old_animals = json.load(read_file)
    old_animals.update(newel)
    with open("animals.json", 'w') as out_file:
        json.dump(old_animals, out_file, indent=4)

with open("animals.json") as in_file:
    newel = json.load(in_file)

print(newel)