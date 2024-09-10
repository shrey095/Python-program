# Create a class with a class attribute a; create an object from it and set ‘a’ 
# directly using ‘object.a = 0’. Does this change the class attribute?
#ans=no the class attribute is not change
class abc:
    a=5

o=abc()
print(o.a) #prints the class attribute because the instance attribute is not present 
o.a=0 #instance attribute is set
print(o.a) #prints the instance attribute because the instance attribute is  present 
print(abc.a)#print the class attribute