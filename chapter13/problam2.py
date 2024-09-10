'''
Write a program to input name, marks and phone number of a student and format it 
using the format function like below: 
 '''

name=input("Enter the Name : ")
marks=int(input("Enter the marks : "))
number=int(input("Enter the Phone Number : "))

a="The name of the student is {}, his marks are {} and phone number is {}".format(name,marks,number)

print(a)