a = int(input("enter ur age: "))

if a >= 18:
    print("you can vote")
    print("you can drive")
elif a <0:
    print("you are entering an invalid age")
else:
    print("you can't vote")
    print("you can't drive")