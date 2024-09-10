# Write a program to find the greatest of four numbers entered by the user. 

a=int(input("Enter the value of A : "))
b=int(input("Enter the value of B : "))
c=int(input("Enter the value of C : "))
d=int(input("Enter the value of D : "))

if(a>b and a>c and a>d):
    print("A is Max",a)
elif(b>a and b>c and b>d):
    print("B is Max",b)
elif(c>a and c>b and c>d):
    print("C is Max",c)
elif(d>a and d>b and d>c):
    print("D is Max",d)
# else:
    # print("D is Max",d)