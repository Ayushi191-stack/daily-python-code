class Employee:
    a = 1

    @classmethod
    def show(cls):
        print(f"The class attribute of a is {cls.a}")

    @property
    def name(self):
        return   (f"{self.fname} {self.lastname}")
    
    @name.setter
    def name(self, value):
        self.fname = value.split(" ")[0]
        self.lastname = value.split(" ")[1]

e = Employee()
e.a = 45

e.name = "John Doe"