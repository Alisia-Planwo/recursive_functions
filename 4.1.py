nested_dict = {
    "a": 1,
    "b": {"x": 2, "y": {"z": 3}},
    "c": {"x": 4}
}

def update(dic,target_key,new_value):
    for key,value in dic.items():
        if key==target_key:
            dic[key]=new_value
        elif isinstance(value,dict):
            update(value,target_key,new_value)
    return dic
print(update(nested_dict,"a",100))
