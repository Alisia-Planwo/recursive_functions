def depth(data):
    if isinstance(data,dict):
        return 1 + max((depth(values) for values in data.values()),default=0)

    elif isinstance(data,list):
        return 1 + max((depth(items) for items in data),default=0)

    else:
        return 0

nested_dict = {'a': 1, 'b': {'c': {'d': 4, 'e': {'f': 6}}}}
nested_list = [1, [2, [3, [4]]]]
print("Depth of nested_dict:", depth(nested_dict))
print("Depth of nested_list:", depth(nested_list))



