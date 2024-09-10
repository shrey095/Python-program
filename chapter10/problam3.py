# Write a class “Calculator” capable of finding square, cube and square root of a 
# number
# Add a static method in problem 2, to greet the user with hello. 
class Calculato:
    '''def __init__(self,square,cube,square_root):
        self.square= square*square #square**2
        self.cube=cube*cube*cube #cube**3
        self.square_root=square_root**1/2  #it is not proper ans for square root of the number
'''    
    def __init__(self,n):
        self.n=n
    
    def square(self):
        print(f"The Square of the {self.n} number = {self.n*self.n}")

    def cube(self):
        print(f"The cube of the {self.n} number = {self.n*self.n*self.n}")
  
    def squareroot(self):
        print(f"The Square root of the {self.n} number = {self.n**1/2}")#it is worng ans and this logic is worang

    @staticmethod
    def greet():
        print("Hello")

# a=Calculato(2,3,4)
# print(a.square,a.cube,a.square_root)

a=Calculato(9)
a.square()
a.cube()
a.squareroot()
a.greet()