#  Create a class (2-D vector) and use it to create another class representing a 3-D 
# vector.
class TwoDVector:
    
    def __init__(self, i, j):
        self.i = i
        self.j = j

    def show(self):
        print(f"The 2-D vector = {self.i}i + {self.j}j")

class ThreeDVector(TwoDVector):

    def __init__(self, i, j, k):
        super().__init__(i, j)  # Call the TwoDVector constructor
        self.k = k

    def show1(self):
        print(f"The 3-D vector = {self.i}i + {self.j}j + {self.k}k")

a = TwoDVector(4, 3)
a.show()

b = ThreeDVector(3, 4, 5)
b.show1() 
