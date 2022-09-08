list_dicts_1 = [
    {"x": 10},
    {"x": 5},
    {"x": 7}
    ]

list_dicts_2 = [
    {"x": 10},
    {"x": 3},
    {"x": 7}
    ]

print(next((item for item in list_dicts_1 if item["x"] == 5), {}))
print(next((item for item in list_dicts_2 if item["x"] == 5), {}))