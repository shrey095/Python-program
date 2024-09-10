# Write a program to filter a list of numbers which are divisible by 5.
def div5(n):
    if(n%5==0):
        return True
    return False

a=[1,5,7,10,43,55,95,2,3,4]

fiv=filter(div5,a)
print(list(fiv))

