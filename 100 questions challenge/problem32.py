#count frequency using dictionary
lst = [1, 2, 3, 2, 1, 2, 4]

freq = {}

for item in lst:
    if item in freq:
        freq[item] += 1
    else:
        freq[item] = 1

print(freq)