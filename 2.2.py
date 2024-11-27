def reverse_list(input_list):
    rev=[]
    for i in reversed(input_list):
        if isinstance(i,list):
            rev.extend(reverse_list(i))
        else:
            rev.append(i)

    return rev

input_list=[[1, 2, [3]], 4, [[5, 6], 7]]
print(reverse_list(input_list))
