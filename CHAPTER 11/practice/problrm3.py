#create a class 'Employee' and add sallry and increment properties to it
class Employee:
    salary = 10000
    increment = 1.5
    incrementted_salary = salary + ((salary * increment)/100)

e = Employee()
print(e.salary)
print(e.increment)
print(e.incrementted_salary)