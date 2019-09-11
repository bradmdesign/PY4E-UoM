
import json

input = '''[
    {
    "id" : "001",
    "x" : "002",
    "name" : "Brad"
    },
    {
    "id" : "009",
    "x" : "7",
    "name" : "Chuck"
    }

]'''


info = json.loads(input)
print("User Count:", len(info))

for item in info:
    print("ID: ",item["id"])
    print("Name: ",item["name"])
    print("Attribute: ",item["x"])
    if item["name"] == "Chuck":
        print("Chuck found")