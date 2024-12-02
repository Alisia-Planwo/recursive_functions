def replace(data,old_value,new_value):
    if isinstance(data,list):
        return [replace(i,old_value,new_value) for i in data]

    elif isinstance(data,dict):
        return {key:replace(value,old_value,new_value) for key,value in data.items()}

    else:
        return new_value if data==old_value else data

nested_data = {
    "a": [1, 2, {"b": 3, "c": [4, 1]}],
    "d": 1,
    "e": {"f": 1, "g": [1, 2]}
}

result = replace(nested_data, 1, "one")
print(result)
