##Topic: Basic & Numbers
# Question 1: Print hello world by using different methods
print("Hello World")
    #or
hello = input("Enter your words: ")
print(hello)

  #or
def greet():
    greeting = "hello world"
    return greeting

a = greet()
print(a)
    #or by class method
class Hello:
    def show(self):
        print("Hello, world")

obj = Hello
obj.show()
#or by static method
class Hello:
    @staticmethod
    def show():
        print("Hello world")

Hello.show()

