#character counter
#A Character Counter program counts how many times each character appears in a string
text = input("Enter a string: ")

char_count = {}

for ch in text:
    if ch in char_count:
        char_count[ch] += 1
    else:
        char_count[ch] = 1

print(char_count)
#or using count
text = input("Enter a string: ")

for ch in set(text):
    print(ch, ":", text.count(ch))