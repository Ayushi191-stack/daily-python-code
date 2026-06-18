#student mark system
Name = input("Enter the student name:")
sub1 = int(input("enter the maths number:"))
sub2 = int(input("enter the physics number:"))
sub3 = int(input("enter the chemistry number:"))
total = sub1 + sub2 + sub3
average = total/3
percentage = average*100
print(percentage)
if percentage >= 80:
    print("Greade A")
elif percentage  >= 60:
    print("Grade B")
elif percentage >= 40:
    print("Grade C")
else:
    print("failed")