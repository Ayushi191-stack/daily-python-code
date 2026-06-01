word = "Donkey"

with open("file.txt", "r") as f:
    content = f.read()

contentNew = content.replace("Donkey", "####")

with open("file.txt", "w") as f:
    f.write(contentNew)

#python in  which line number
with open("log.txt") as f:
    lines = f.readlines()
lineno = 1
for line in lines:
    if "python" in line:
        print(f"Yes, python is present in line {lineno}")
    lineno += 1
else:
    print("No, python is not present in the file")