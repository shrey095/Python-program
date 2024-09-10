'''
Write a python function to print first n lines of the following pattern: 
*** 
**        - for n = 3       
* 
'''
n= int(input("Enter the value of N : "))
def patt():
    for i in range(0,n):
        print("*"*(n-i))
patt()

# exter using recarson
# def pattern(n):
#     if(n==0):
#         return
#     print("*"*n)
#     pattern(n-1)

# pattern(5)
    
