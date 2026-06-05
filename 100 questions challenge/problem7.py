#Palindrone number
# A palindrome reads the same from both directions. Your task is to check whether the given input satisfies this property
def palindrome(num):
    return num == num[:: -1]

print(palindrome("mam"))
    #or
num = input("Enter a number: ")
if (num == num[:: -1]):
    print("it's a palindrome ")

else:
    print("it's not")