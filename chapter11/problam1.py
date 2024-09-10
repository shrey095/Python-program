# it is Single inheritance 
'''class Employee:
    compay="ITC"
    name="abcd"
    def show(self):
        print(f"The name of Employee is {self.name}")

class programmer(Employee):
    compay="ITC Infotech"
    lan="Python"
    def showlan(self):
        print(f"The name is {self.name} and he is good in {self.lan} Language")
    
a=programmer()
a.show()
a.showlan()'''

# it is Multiple inheritance
'''
class Employee:
    compay="ITC"
    name="abcd"
    def show(self):
        print(f"The name of Employee is {self.name}")

class coder:
    lan="Python"
    def prisho(self):
        print(f"Hear is your Language : {self.lan}")

class programmer(Employee,coder):
    compay="ITC Infotech"
    def showlan(self):
        print(f"The name is {self.name} and he is good in {self.lan} Language")
    
a=programmer()
a.show()
a.prisho()
a.showlan()'''

# it is Multilevel inheritance 
class Employee:
    compay="ITC"
    name="abcd"
    def show(self):
        print(f"The name of Employee is {self.name}")

class coder(Employee):
    lan="Python"
    def prisho(self):
        print(f"Hear is your Language : {self.lan}")

class programmer(coder):
    compay="ITC Infotech"
    def showlan(self):
        print(f"The name is {self.name} and he is good in {self.lan} Language")
    
a=programmer()
a.show()
a.prisho()
a.showlan()

