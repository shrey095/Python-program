# Write a program to print multiplication table of n using for loops in reversed 
# order. 
num = int(input("Enter the value of N : "))
for i in range(1,11):
    print(f"{num} x {11-i} = {num*(11-i)}")

'''
1 10 = 1+10 = 11
2 9  = 2+9 =  11
3 8  = 3+8 =  11
..
10 1 = 1+10 = 11
hear we can see the sum of this patten is 11 thatway we writ 11-i in over logic
'''