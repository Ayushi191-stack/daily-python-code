#BMI calculator
weight = float(input("Enter ur weight:"))
height = float(input("Enter ur height:"))
BMI = weight/(height*height)
print(BMI)
if BMI < 18.5:
    print("underweight")
elif BMI >= 18.5 and BMI <=24.9:
    print("Normal weight")
elif BMI >= 25 and BMI <= 29.9:
    print("overweight")
elif BMI > 30:
    print("obese")