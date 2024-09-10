# st="abcdeeij vjergldtib ivlibf rwitdlibgftbijgf"
# f=open("file1.txt","w")
# f.write(st)
# f.close()

# f=open("file1.txt")
# print(f.read())
# f.close()

# the same can be written using with statment lick this:
with open("file1.txt") as f:
    print(f.read())
#  you don't have to explicitly close the file