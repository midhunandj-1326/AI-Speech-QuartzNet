import json

with open("dataset_info.json","r") as f:
    data = json.load(f)

print(type(data))
print(data)