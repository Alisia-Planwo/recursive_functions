def compute_sum(structures):
    total=0
    if isinstance(structures,list):
        for i in structures:
            total+=compute_sum(i)
    elif isinstance(structures,dict):
        for v in structures.values():
            total+=compute_sum(v)
    elif isinstance(structures,(int,float)):
        total+=structures
    return total

structures=[{"a": 1}, [2, {"b": 3}], 4]
print(compute_sum(structures))



