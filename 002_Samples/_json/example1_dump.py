import json

data = {
    'first_name': 'Eugene',
    'last_name': 'Petrov',
    'age': 35,
    'hobbies': [
        'guitar',
        'cars',
        'mountains',
        'adventures'
    ]
}

json_data = json.dumps(data)

with open('output.json', 'w') as f:
    json.dump(data, f)
