import json

students = {
    "dogs": [{
        "id": 0,
        "name": "maja",
        "racce": "dog",
    }, {
        "id": 1,
        "name": "milus",
        "racce": "dog",
    }],
    "cats": [{
        "id": 0,
        "name": "puszek",
        "racce": "cat",
    }, {
        "id": 1,
        "name": "greebo",
        "racce": "cart",
    }]
}

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


with open("students.json", 'a') as out_file:
    json.dump(students, out_file, indent=2)