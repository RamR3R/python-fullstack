import json
# ['"name": "Alice"' , '"age": 30']
#json obj string => Dict

# converted_list = inp[1: len(inp) - 1]
# converted_list = converted_list.split(",")
result = {}



# for i in converted_list:
#     # "name": "Alice"
#     key_value = i.split(":")
#     # ["name" , "Alice"]
#     key_value[0] = key_value[0].strip()[1:len(key_value[0])-1]
#     key_value[1] = key_value[1].strip()[1:len(key_value[1])-1]
#     result[key_value[0]] = key_value[1]

inp =  '{"name": "Alice", "age": 30}'
result = json.loads(inp) #jsonString to dict
result = json.dumps(result) #dict to JSON string
print(type(result))
