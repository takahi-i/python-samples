from collections import defaultdict
d = defaultdict(int)

for key in ["foo", "bar", "baz"]:
    d[key] += 1

print(dict(d))
