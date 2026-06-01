#file1 content is identical to file2 content
with open("file1.txt") as f:
    content1 = f.read()

with open("file2.txt") as f:
    content2 = f.read()

if content1 == content2:
    print("The contents of file1.txt and file2.txt are identical.")
else:
    print("The contents of file1.txt and file2.txt are not identical.")