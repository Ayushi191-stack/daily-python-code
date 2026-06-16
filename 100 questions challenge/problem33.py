#merge two dict
dict1 = {
    "play": "khelna",
    "eat" : "khana"
    }
dict2 = {
    "go": "jaana",
    "come": "aana"
}
merged = dict1 | dict2
print(merged)