#inverted dict
d = {
    "a": 1,
    "b": 2,
    "c": 3
}

inverted = {}

for key, value in d.items():
    inverted[value] = key

print(inverted)