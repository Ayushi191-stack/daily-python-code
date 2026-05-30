#wriite a program to read the text from a give file 'poems.txt' and find out whether the word 'twinkle' is present in the file or not. If it is present then print 'twinkle is present' otherwise print 'twinkle is not present'
f = open("CHAPTER 9/poems.txt")
data = f.read()
if "twinkle" in data:
    print("twinkle is present")
else:
    print("twinkle is not present")
f.close()