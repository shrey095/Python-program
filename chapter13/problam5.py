# Write a program to find the maximum of the numbers in a list using the reduce 
# function.
from functools import reduce 
l=[1,5,7,10,43,55,95,2,3,4]

def get(a,b):
    if(a>b):
        return a
    return b

print(reduce(get,l))
