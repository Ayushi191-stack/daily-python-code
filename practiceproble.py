# 5!=1*2*3*4*5 factorial
n = int(input("enter a number: "))
factorial = 1
for i in range(1,n+1):
    factorial = factorial*i
print(factorial)


# star pattern
n = int(input("enter a number: "))
for i in range(1,n+1):
    print("*"*i)

n = int(input("enter a number: "))
for i in range(1,n+1):
    print(" "*(n-i),end="")
    print("*"* (2*i-1),end="")
    print("")

n =  int(input("enter a number: "))
for i in range(1,n+1):
    if(i == 1 or i == n):
        print("*"*n, end="")
    else:
        print("*", end="")
        print(" "*(n-2), end="")
        print("*", end="")
        print("")

# reverse table
n = int(input("enter a number: "))
for i in range(10,0,-1):
    print(f"{n} x {i} = {n*i}")
     #or
n = int(input("enter a number: "))
for i in range(1,11):
    print(f"{n} x {11-i} = {n*(11-i)}")