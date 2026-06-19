#ATM wuthdrawal simulation
balance = 5000

amount = int(input("Enter withdrawal amount:"))

if amount <= balance:
    balance = balance - amount
    print("withdrawal successful")
    print("Remaining balance",balance)
else:
    print("insufficient balance")