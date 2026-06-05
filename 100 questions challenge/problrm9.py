#REverse a num
num = input("Enter a number: ")
print("The reverse of a number is: ",num[::-1]) # by myself

#or
num = int(input("Enter a nnumber: "))

reverse = 0

while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num //= 10

print("The reverse number is:", reverse)

