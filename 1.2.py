def count_list(lst):
    count=0
    for i in lst:
        if isinstance(i,list):
            count+=count_list(i)
        else:
            count+=1

    return count

lst=[1,2,[9,8,89],7]
print(count_list(lst))