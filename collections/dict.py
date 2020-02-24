d = {}

for key in ["foo", "bar", "baz"]:
    if key not in d:
        d[key] = 0
    d[key] += 1


print(d)
