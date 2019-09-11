import json

data = ''' {
    "name" : "Chuck",
    "phone" : {
        "type": "intl",
        "number" : "+1 234 412 4122"
    },
    "email" : {
        "hide" : "yes"
    }
}'''

info = json.loads(data)

#info is like a dictionary
print('Name:',info["name"])
print('Hide:',info["email"]["hide"])
print('Phone:',info["phone"]["number"])