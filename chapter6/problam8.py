# Write a program to find out whether a given post is talking about “Ram” or not. 
name=input("Enter the Post : ")
if("Ram".lower() in name.lower()):    #hear we use lower funcation because we convart over input string to lowercase and than camper  
    print("This post is talking about “Ram”")
else:
    print("This post is not talking about “Ram”")