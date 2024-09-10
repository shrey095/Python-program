'''
We are going to write a program that generates a random number and asks the user to 
guess it. 
If the player’s guess is higher than the actual number, the program displays “Lower 
number please”. Similarly, if the user’s guess is too low, the program prints “higher 
number please” When the user guesses the correct number, the program displays the 
number of guesses the player used to arrive at the number. 
Hint: Use the random module.

'''
import random 
x=random.randint(1,100)
guesses=1
n=-1

while(n!=x):
    n=int(input("Enter the Number which you guess : "))
    if(n>x):
        print("Lower number please")
        guesses+=1
    elif(n<x):
        print("Higher number please")
        guesses+=1

print(f"You have guessed the number {n} correctly in {guesses} attempts")