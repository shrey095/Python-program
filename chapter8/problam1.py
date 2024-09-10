# funcation Definition
def GoodDay():
    print("Hello Friends,My name is Shrey")
# funcation calling
GoodDay()
GoodDay()
print("------------------------------")
# funcation with parameter and return 
def f1(name,str):
    print("Good day,"+name)
    print(str)
    return "Fine"
a=f1("Rahil","How are you")
print(a)
b=f1("Kavish","How are you")
print(b)
print("------------------------------")
# default PARAMETER VALUE
def f2(name,str="Thanks"):
    print("Good day,"+name)
    print(str)
f2("Ram","Thankyou")
f2("Ome")

def factorial(n):
    if(n==0 or n==1):
        return 1
    return n*factorial(n-1)

n=int(input("Enter the value of N : "))
print(f"The factorial of {n} = {factorial(n)}")
# How do you prevent a python print() function to print a new line at the end.
print("A")
print("B")
print("C")
print("D",end="")
print("E",end="")