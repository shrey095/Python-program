#  A file contains a word “Donkey” multiple times. You need to write a program 
# which replace this word with ##### by updating the same file. 
word="Donkey"
with open("file2.txt","r") as f:
    content=f.read()

Newcontent=content.replace(word,"######")

with open("file2.txt","w") as f:
    f.write(Newcontent)

