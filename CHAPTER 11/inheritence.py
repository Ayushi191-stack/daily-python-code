class Employee:
    company = "ITC"
    def show(self):
        print(f"The name of the Employee is {self.name} and the company is {self.company}")

class Programmer(Employee):
    company = "ITC Infotech"
    def showLanguage(self):
        print(f"The name is {self.name} and he is good with the language is {self.language}")

a = Employee()
b = Programmer()

print(a.company,b.company)