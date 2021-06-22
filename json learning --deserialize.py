# Python program to read
# json file


import json

# Opening JSON file
f = open('data_file.json', )

# returns JSON object as
# a dictionary
data = json.load(f)

data.update('user'['colour':'pleasant pink'])

print(data)



# # Iterating through the json
# # list
# for i in data:
#     print(i)

# Closing file
f.close()