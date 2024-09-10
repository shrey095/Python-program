class Employee:
    language="Python" #This is a class attribute
    salary=1200000

    def getinfo(self):
       
        print(f"Lanaguage = {self.language},Salary = {self.salary}")

    @staticmethod
    def good():
        print("Good day Brooooo")
    
    def __init__(self,language,salary,name):    # it id dunder method and this method is automatically called   
        self.name=name
        self.language=language
        self.salary=salary
        print("hello friends") 
       

a=Employee("Java",1500000,"ABC")  
#a.language="java"  # This is a in INSTANCE ATTRIBUTES
a.getinfo()
a.good()
print(a.name,a.language,a.salary)
# Employee.getinfo(a)