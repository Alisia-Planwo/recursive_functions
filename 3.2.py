data = [
    {"x": 10, "y": 20},
    {"z": 30},
    {"x": 40, "w": 50},
    {"y": 60, "z": 70}
]

unique={key for i in data for key in i}
unique_lst=list(unique)
print(unique_lst)

