#  Write a class vector representing a vector of n dimensions. Overload the + and * 
# operator which calculates the sum and the dot(.) product of them.
class Vector:
    def __init__(self,i,j,k):
        self.i=i
        self.j=j
        self.k=k
    
    def __add__(self,a1):
        ans=Vector(self.i+a1.i,self.j+a1.j,self.k+a1.k)
        return ans
    
    def __mul__(self,a1):
        ans=self.i*a1.i+self.j*a1.j+self.k*a1.k
        return ans
    
    def __str__(self):
        return f"Vector({self.i},{self.j},{self.k})"
    
v1=Vector(1,2,3)
v2=Vector(4,5,6)

print(v1+v2)
print(v1*v2)