def count_str(data):
    count=0
    if isinstance(data,list):
        for i in data:
            count+=count_str(i)
    elif isinstance(data,dict):
        for v in data.values():
            count+=count_str(v)
    elif isinstance(data,str):
        count+=1
    return count

data = [{"a": "hello"}, ["world", {"b": "Python"}], 42, "AI"]
print(count_str(data))