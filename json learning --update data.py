import json

a_file = open("data_file.json", "r")
json_object = json.load(a_file)
a_file.close()

json_object['user']["d_size"] = 17

a_file = open("data_file.json", "w")

json_object['user2'] = {
    "name" : "Sir Fuzzy Balls III",
    "age": 55
    }


json.dump(json_object, a_file, indent=4)
a_file.close()

json_str = json.dumps(json_object, indent=4)

print(json_str)
print(type(json_str))
