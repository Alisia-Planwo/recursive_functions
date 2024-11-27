def integers(input_list):
    sm=[]
    for i in input_list:
        if isinstance(i,int):
            sm.append(i)
        elif isinstance(i,list):
            sm.extend(integers(i))
    return sm

input_list=[1, [2, "a", [3]], "b", [4, [5]]]
print(integers(input_list))
