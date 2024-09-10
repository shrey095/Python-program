# Store the multiplication tables generated in problem 3 in a file named Tab.txt. 
n=int(input("Enter the Number : "))
table=[n*i for i in range(1,11)]
print(table)
with open("Tab.txt","a") as f:
    f.write(f"Table of {n} no : {str(table)}\n")