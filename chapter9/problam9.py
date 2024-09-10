# Write a program to find out whether a file is identical & matches the content of 
# another file. 
with open("file1.txt","r") as f:
    contant1=f.read()
with open("file2.txt","r") as f:
    contant2=f.read()

if(contant1==contant2):
    print("Yes these files are identical")
else:
     print("No these files are not  identical")