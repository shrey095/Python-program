num=int(input("Enter the Number : "))
for i in range(1,11):
    # table=num*i
    # print(num,"*",i,"=",table)
    print(f"{num} x {i} = {num*i}") #we use fstring
    
print("--------------------------------------------------------")
i=1
while(i<=10):
    print(f"{num} x {i} = {num*i}")
    # i=i+1
    i+=1