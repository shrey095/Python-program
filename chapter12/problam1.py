from typing import List,Tuple,Union,Dict 
# WALRUS OPERATOR 
if(n:=len([1,4,2,5,7])) > 3:
   print(f"List is too long ({n} elements, expected <= 3)") 

n : int =5
a : str = "cvf"

def sum(i : int,j : int) -> int:
   return i+j

sum(5,3)

l:list[int]=[1,2,3,4,5]
t:tuple[str]=("fckv","rfuvdj")
d:dict[int,str]={1:"sfw",2:"erfssv"}

def Riv(lilili):
   match lilili:
      case 200:
         return "Hello"
      case 400:
         return "Helooooooooooooo"
      case 500:
         return "ok Know ......."
      case _:
         return "inviled llalala"
    
print(Riv(200))

d1={1:"eads",2:"wed"}
d2={3:"esdcf",4:"wfcs"}
m=d1|d2
print(m)

try:
   n=int(input("Enter the  a : "))
except ValueError as v:
   print(v)
except ZeroDivisionError as z:
   print(z)
except Exception as e:
    print(e)
    
print("wesedsc")