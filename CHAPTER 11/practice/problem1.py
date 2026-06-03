#create a class (2-D vector) and use it to create another class represnting a 3-D vector
class TwoDVector:
    def __init__(self, i, j):
        self.i = i
        self.j = j

    def show(self):
        print(f"The vector is: {self.i}i + {self.j}j")

class ThreeDVector(TwoDVector):
    def __init__(self, i, j, k):
        super().__init__(i, j)
        self.k = k

    def show(self):
        print(f"The vector is: {self.i}i + {self.j}j + {self.k}k")

v1 = TwoDVector(1, 2)
v1.show()
v2 = ThreeDVector(1, 2, 3)
v2.show()
