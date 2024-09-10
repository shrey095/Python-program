#  Write a python program to rename a file to “renamed_by_ python.txt. 
with open("old.txt","r") as f:
    contant=f.read()
with open("renamed_by_ python.txt","w") as f:
    f.write(contant)

# in this progam we can first copy tha contant of file 1 into file 2 and than delete tha
# file 1 from over pc