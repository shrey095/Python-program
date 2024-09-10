# Write a program using functions to find greatest of three numbers. 

a=int(input("Enter the value of Number 1 : "))
b=int(input("Enter the value of Number 2 : "))
c=int(input("Enter the value of Number 3 : "))

def greatest():
    if(a>b and a>c):
        return a
    elif(b>a and b>c):
        return b
    elif(c>a and c>b):
        return c    

print(f"The greatest of three numbers = {greatest()}")