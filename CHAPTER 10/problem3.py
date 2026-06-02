#create an object from it and set 'a' directly using object.a = o. Does tgis change the class attributr?
class Demo:
    a = 4

o = Demo()
print(o.a) # This will print 4, which is the class attribute
o.a = 0
print(o.a) # This will print 0, which is the instance attribute
print(Demo.a) # This will print 4, which is the class attribute