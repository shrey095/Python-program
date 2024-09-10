# Write a program to display a/b where a and b are integers. If b=0, display infinite by 
# handling the ‘ZeroDivisionError’.

try:
    a= int(input("Enter the value of A : "))
    b= int(input("Enter the value of B : "))
    print(f"The divison of a/b = {a/b}")

except ZeroDivisionError as z:
    print("Infinite")