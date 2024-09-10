'''
We all have played snake, water gun game in our childhood. If you haven’t, google the 
rules of this game and write a python program capable of playing this game with the 
user. 
'''
import random

print("-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-")
print("s for Snake")
print("w for Water")
print("g for Gun")
print("-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-")

you=input("Enter your Choice : ")

youDic={"s":1,"w":-1,"g":0}
reversDic={1:"Snake",-1:"Water",0:"Gun"}

computer = random.choice([-1,0,1])

user=youDic[you]

print("-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-")
print(f"Your Choice = {reversDic[user]}\nComputer Choice = {reversDic[computer]}")
print("-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-")

if(computer==user):
    print("Match is Drow")
else:
    '''
    if(computer==-1 and user==1): (computer-user) = -2
        print("You win!")
    elif(computer==-1 and user==0):(computer-user) =-1
        print("You lose!")
    elif(computer==1 and user==-1):(computer-user) =2
        print("You lose!")
    elif(computer==1 and user==0):(computer-user) =1
        print("You win!")
    elif(computer==0 and user==-1):(computer-user) =1
        print("You win!")
    elif(computer==0  and user==1):(computer-user) =-1
        print("You lose!")
    else:
        print("Inviled Choice")
    '''

    # the below logic is written on the basis of value of computer-user  
    if((computer - user) == -1 or (computer - user) == 2):
        print("You lose!")
    else:
        print("You win!")