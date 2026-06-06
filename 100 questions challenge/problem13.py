#chech palindrome string
num = input("Enter a string: ")
if num == num[::-1]:
    print("yes,it's a palindrome")
else:
    print("it's not")