import json

a_file = open("data_file.json", "r")
json_object = json.load(a_file)
a_file.close()
print(json_object)

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

# Python program to update
# JSON


# import json
#
# # JSON data:
# x =  { "organization":"GeeksForGeeks",
#         "city":"Noida",
#         "country":"India"}
#
# # python object to be appended
# y = {"pin": 12345}
#
# a_file = open("data_file.json", "r")
# z = json.load(a_file)
#
# # parsing JSON string:
# # z = json.load(data_file.json)
#
# # appending the data
# z.update(y)
#
# # the result is a JSON string:
# print(json.dumps(z))