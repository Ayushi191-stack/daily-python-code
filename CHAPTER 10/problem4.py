#add static method to problem2
class Calculator:
    def __init__(self,n):
        self.n =n

    def square(self):
        print(f"The sqaure is {self.n*self.n}")

    def cube(self):
        print(f"The cube is {self.n*self.n*self.n}")

    def sqaureroot(self):
        print(f"The square root is {self.n**0.5}")

    @staticmethod
    def hello():
        print("Hello, I am a static method")

num = Calculator(4)
num.square()
num.cube()
num.sqaureroot()
num.hello()
  