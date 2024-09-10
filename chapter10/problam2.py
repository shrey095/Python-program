# Create a class “Programmer” for storing information of few programmers 
# working at Microsoft. 
class Programmer:
    company="Microsoft"
    def __init__(self,name,salary,id):
        self.name=name
        self.salary=salary
        self.id=id

a=Programmer("abc",12345,1) 
b=Programmer("bcd",123567,2) 
c=Programmer("cde",123499,3) 

print(a.id,a.name,a.salary,a.company)
print(b.id,b.name,b.salary,b.company)
print(c.id,c.name,c.salary,c.company)
