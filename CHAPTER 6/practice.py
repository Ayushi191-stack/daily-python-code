a = int(input("enter a number: "))
b = int(input("enter another number: "))
c = int(input("enter another number: "))
d = int(input("enter another number: "))

if a > b and a > c and a > d:
    print("a is greatest")
elif b > a and b > c and b > d:
    print("b is greatest")
elif c > a and c > b and c > d:
    print("c is greatest")
else:
    print("d is greatest")


#q2
maths = int(input("enter your maths marks: "))
physics = int(input("enter your physics marks: "))
chemistry = int(input("enter your chemistry marks: "))

total_marks = maths + physics + chemistry
percentage = (total_marks/300)*100
print("your percentage is:", percentage)

if percentage >= 40:
    print("you have passed")
elif percentage >= 33 and percentage < 40:
    print("you have just passed")
else:
    print("you have failed")

#q3
text = input("enter a string: ")

if text == "make a lot of money" or text == "buy now" or text == "subscribre this" or text == "click this":
    print("you are a spammer")
else:
    print("you are not a spammer")

#q4
post = input("enter your post: ")

if ("Ayushi".lower() in post.lower()) :
    print("post is talking about Ayushi")
else:    
    print("post is not talking about Ayushi")