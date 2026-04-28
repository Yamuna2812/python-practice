d1 = {"a": 1, "b": 2}
d2 = {"b": 3, "c": 4}

for key, value in d2.items():
    d1[key] = d1.get(key, 0) + value

print(d1)