# Python program to read
# json file


import json

# Opening JSON file
f = open('data_file.json', )

# returns JSON object as
# a dictionary
data = json.load(f)

# Iterating through the json
# list
for i in data['user']:
    print(i)

# Closing file
f.close()