import json

json_data = '{"first_name": "Eugene"}'
data = json.loads(json_data)
print(data)
print(type(data))

with open('output.json', 'r') as f:
    data = json.load(f)
    print(data)
    print(type(data))
