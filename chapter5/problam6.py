# Create an empty dictionary. Allow 4 friends to enter their favorite language as 
# value and use key as their names. Assume that the names are unique. 

a={}
name= input("Enter the Friend Name   : ")
lang= input("Enter the Language Name : ")
a.update({name:lang})
name= input("Enter the Friend Name   : ")
lang= input("Enter the Language Name : ")
a.update({name:lang})
name= input("Enter the Friend Name   : ") 
lang= input("Enter the Language Name : ")
a.update({name:lang})
name= input("Enter the Friend Name   : ")
lang= input("Enter the Language Name : ")
a.update({name:lang})

print(a)

# 1)If the names of 2 friends are same; what will happen to the program in problem 
b={}
name= input("Enter the Friend Name   : ")
lang= input("Enter the Language Name : ")
b.update({name:lang})
name= input("Enter the Friend Name   : ")
lang= input("Enter the Language Name : ")
b.update({name:lang})
name= input("Enter the Friend Name   : ") 
lang= input("Enter the Language Name : ")
b.update({name:lang})
print(b)
name= input("Enter the SameFriend Name   : ")
lang= input("Enter the Language Name : ")
b.update({name:lang})

print(b)
# ans = the 2 friend name same ok no problam but that key is update that friend key is last update key

# 2)If languages of two friends are same; what will happen to the program in problem 
c={}
name= input("Enter the Friend Name   : ")
lang= input("Enter the Language Name : ")
c.update({name:lang})
name= input("Enter the Friend Name   : ")
lang= input("Enter the Language Name : ")
c.update({name:lang})
name= input("Enter the Friend Name   : ") 
lang= input("Enter the Language Name : ")
c.update({name:lang})
name= input("Enter the Friend Name   : ")
lang= input("Enter the SameLanguage Name : ")
c.update({name:lang})

print(c)
# ans = hear we can update tha key and the key are same but it is (not possibley) not vilied in some time