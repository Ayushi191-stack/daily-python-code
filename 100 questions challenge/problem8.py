#Armstrong number
#An Armstrong number (also called a narcissistic number) is a number that is equal to the sum of its digits raised to the power of the number of digits.
num = input("Enter a number: ")
a = len(str(num))
print(a)
b = str(num)[0]
print(b)
c = str(num)[1]
print(c)
d = str(num)[2]
print(d)
Arm = (int(b)**a + int(c)**a +int(d)**a)# we can't add,sub,mult etc a string with any integer so use int(a)
print("The armstrong no is:",Arm)
if int(num) == Arm: #num is a string while Arm is a integer we can equate them withount converting num into integer
    print("it's an Armstrong number")
else:
    print("it's not") # it's done by me
    #or
#2nd one is refrence from chatgpt
num = int(input("Enter a  number: "))

order = len(str(num))
temp = num
sum  = 0

while temp > 0:
    digit = temp % 10
    sum += digit ** order
    temp //= 10

if sum == num:
    print("it's a armstrong no.")
else:
    print("it's not")
