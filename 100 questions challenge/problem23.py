#Find second Largest number
a = int(input("Enter 1st number: "))
b = int(input("Enter 2nd number: "))
c = int(input("Enter 3rd number: "))
if (a>=b>=c) or (c >= b >= a):
    print("b is the second largest no.")

elif(b>=a>=c) or (c >= a >= b):
    print("a is the second largest")

else:
    print("c is the second largest")