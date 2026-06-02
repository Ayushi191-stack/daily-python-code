class Employee:
    name = "Harry" # Class attribute
    language = "Python"
    salary = 100000

    def __init__(self): #dunder method which is automatically called when an object is created
        print("Employee object created")

    def getInfo(self):
        print(f"Name: {self.name}, Language: {self.language}, Salary: {self.salary}")

    def greet(self):
        print("Good morning")


Ayushi = Employee()
Ayushi.name = "Ayushi Raj" # Instance attributes
print(Ayushi.name, Ayushi.language, Ayushi.salary)
Ayushi.getInfo()
Ayushi.greet()