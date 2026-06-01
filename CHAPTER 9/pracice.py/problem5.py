#repeat program 444 for a list of such words to be censored
word = ["Donkey","bad","ugly"]

with open("file.txt", "r") as f:
    content = f.read()


for w in word:
    content = content.replace(w, "####")

with open("file.txt", "w") as f:
    f.write(content)