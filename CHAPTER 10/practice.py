#create a class "programmer" for storing information of feew programmers working in microsoft.
class Programmer:
    name = "Ayushi RAj"
    company = "Microsoft"
    salary = 120000

    def getInfo(self):
      print(f"Name: {self.name}, Company: {self.company}, Salary: {self.salary}")
Ayushi = Programmer()
Ayushi.getInfo()

Aditya = Programmer()
Aditya.name = "Aditya Raj"
Aditya.getInfo()