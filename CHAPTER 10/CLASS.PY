class Employee:
    name = "Harry" # Class attribute
    language = "Python"
    salary = 100000


Ayushi = Employee()
Ayushi.name = "Ayushi Raj" # Instance attributes
print(Ayushi.name, Ayushi.language, Ayushi.salary)

#instance attribute will take over the class attribute
