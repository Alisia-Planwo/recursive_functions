def nested_list(lst):
    max_value=float('-inf')

    for i in lst:
        if isinstance(i,list):
            max_value=max(max_value,nested_list(i))
        else:
            max_value=max(max_value,i)

    return max_value

print(nested_list([1,2,[4,5,6],10]))




