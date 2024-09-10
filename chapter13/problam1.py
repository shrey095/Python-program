from functools import reduce 
cube= lambda x : x**3
squer= lambda x : x*x

print(cube(5))
print(squer(5))


a=["aaahswja","eefds","edfr"]

f="-".join(a)
print(f)

a="{} is a good {}".format("Abc", "boy")
print(a)

a="{0} is a good {1}".format("Abc", "boy")
print(a)

a="{1} is a good {0}".format("Abc", "boy")
print(a)
print("\n\n")

l=[1,2,3,4,5]

sq = lambda c : c*c
s=map(sq,l)

print(list(s))

def even(n):
    if(n%2==0):
        return True
    return False

OEv=filter(even,l)
print(list(OEv))

def sum(a,b):
    return a+b

print(reduce(sum,l))