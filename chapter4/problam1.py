# Unlick string lists are mutable
name=["abcd","apple",12,44.12,True]
print(type(name))
print(name)
print(name[0])
name[0]="hii"
print(name[0])
print(name)
print(name[1:5])
name.append("Hello")
print(name)
l1=[2,5,1,44,5,95,1,32,99,100]
l1.sort()
print(l1)
l1.insert(3,101)
print(l1)
l1.remove(44)
print(l1)

a=(11,43,3,5,89,99,"Abcd","hello")
print(type(a))
