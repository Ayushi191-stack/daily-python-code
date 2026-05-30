st = "Hello, World!"
f = open("myfile.txt", "w")
f.write(st)
f.close()

f = open("file.txt")
lines = f.readlines()
print(lines, type(lines))
f.close()

#you can also read it line by line
f = open("myfile.txt")
line1 = f.readline()
print(line1, type(line1))

line2 = f.readline()
print(line2, type(line2))
f.close()