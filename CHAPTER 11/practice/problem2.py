#create a class 'pets'from a class 'animals' and further create a class "dog" from 'pets' Add a method 'bark' to class 'Dog'
class Animals:
    pass
class Pets(Animals):
    pass

class Dog(Pets):

    @staticmethod
    def bark():
        print("bhau bhau")
d = Dog()
d.bark()
