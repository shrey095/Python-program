# Write a recursive function to calculate the sum of first n natural numbers.
n= int(input("Enter the value of N : "))
def sum(n):
    if(n==0):
        return 0
    elif(n==1):
        return 1
    return sum(n-1)+n
    
print(f"The sum of First {n} natural number =  {sum(n)}")   
# exter
    # if(n==0):
    #     return 0
    # elif(n==1):
    #     return 1
    # return (n*(n+1))/2