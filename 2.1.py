def flat_list(input_list):
    fl=[]
    for i in input_list:
        if isinstance(i,list):
            fl.extend(flat_list(i))
        else:
            fl.append(i)

    return fl

input_list= [[1, 2, [3]], 4, [[5, 6], 7]]
print(flat_list(input_list))