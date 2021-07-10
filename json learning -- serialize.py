import json

data = {"user" :{
    "name" : "Sir Fuzzy Balls III",
    "age": 55
    }
}

data2 = {"user" :{
    "name" : "Sir Fuzzy Balls IV",
    "age": 22,
    }
}

with open('data_file.json','w') as funVarName:
    json.dump(data, funVarName,indent=4)

with open('data_file.json','w') as write_file:
    json.dump(data2, write_file,indent=4)

json_str = json.dumps(data, indent=4)

print(json_str)
print(type(json_str))