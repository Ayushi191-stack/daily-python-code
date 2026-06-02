class Employee:
    def __init__(self):
        print("constructor of employee")
    a = 1
class Programmer(Employee):
    def __init__(self):
        print("constructor of programmer")
    b = 2

class Manager(Programmer):
    def __init__(self):
        super().__init__() # This will call the constructor of the parent class (Programmer)
        print("constructor of manager")
    c = 3

m = Manager()
print(m.a) # This will print 1, which is inherited from Employee
print(m.b) # This will print 2, which is inherited from Programmer
print(m.c) # This will print 3, which is defined in Manager