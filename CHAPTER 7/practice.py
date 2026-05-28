# q1
for i in range(1,11):
    print(i*8)

# q2
l = ["Ayushi", "Riya", "Sakshi", "Pooja", "Shivani"]

for name in l:
    if (name.startswith("S")):
        print(f"Hello {name}")

# q3
n = int(input("enter a number: "))
for i in range(2,n):
    if (n%i )== 0 :
        print("number is  not a  prime number")
        break

    else:
        print("number is a prime number")
        break

#sum of a natural no.
n = int(input("enter a number: "))
sum = 0
i = 1
while i <= n:
    sum += i
    i += 1
    print(sum)
    
        

    
