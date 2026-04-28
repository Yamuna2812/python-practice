data = {"a": 1, "b": 2, "c": 3}

swapped = {v: k for k, v in data.items()}
print(swapped)