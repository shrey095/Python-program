# Write a program to accept marks of 6 students and display them in a sorted manner.
marks=[]
m1=int(input("Enter the Student 1 Marks : "))
marks.append(m1)
m2=int(input("Enter the Student 2 Marks : "))
marks.append(m2)
m3=int(input("Enter the Student 3 Marks : "))
marks.append(m3)
m4=int(input("Enter the Student 4 Marks : "))
marks.append(m4)
m5=int(input("Enter the Student 5 Marks : "))
marks.append(m5)
m6=int(input("Enter the Student 6 Marks : "))
marks.append(m6)

marks.sort()
print(marks)

# Check that a tuple type cannot be changed in python.
a=("rsfvcds","afcsdf",13,95)
a[2]="hello"