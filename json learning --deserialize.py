# program comes from:
# https://www.geeksforgeeks.org/deserialize-json-to-object-in-python/


# importing the module
import json

# creating the JSON data as a string
data = '{"Name" : "Romy", "Gender" : "Female"}'

print("Datatype before deserailization : "
      + str(type(data)))

# deserailizing the data
data = json.loads(data)

print("Datatype after deserailization : "
      + str(type(data)))