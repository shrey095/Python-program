# Write a program to print yes when the age entered by the user is greater 
# than or equal to 18 or print not when age is not greathanthan and equal 18. 
age=int(input("Enter the Age : "))
if(age>=18):
    print("yes")
else:
    print("No")
    
#  Write a program to find the greatest of three numbers entered by the user. 

a=int(input("Enter the value of A : "))
b=int(input("Enter the value of B : "))
c=int(input("Enter the value of C : "))
if(a>b):
    if(a>c):
        print("A is Max")
    else:
        print("C is Max")
else:
    if(b>c):
        print("B is Max")
    else:
        print("C is Max")