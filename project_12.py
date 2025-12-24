import json

user_data  = {
    "name": "Mou",
    "age": 25,
    "gender":"Female"
}

with open("test_data.json","w") as file:
    json.dump(user_data,file)


with open("test_data.json", "r") as file:
    loaded_data = json.load(file)
    print(loaded_data["name"])
