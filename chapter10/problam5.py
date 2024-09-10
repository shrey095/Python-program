#  Write a Class ‘Train’ which has methods to book a ticket, get status (no of seats) 
# and get fare information of train running under Indian Railways.

# Can you change the self-parameter inside a class to something else (say 
# “harry”). Try changing self to “slf”  and see the effects. 
from random import randint
class Train:
    def __init__(slf,trainNo):
        slf.trainNo=trainNo
    
    def book(self,fromm,to):
        print(f"Ticket is booked in train no : {self.trainNo} from {fromm} to {to}")

    def getstatus(self):
        print(f"Train no :{self.trainNo} is running on time")

    def getfare(self,fromm,to):
        print(f"Ticket fare in train no = {self.trainNo} from {fromm} to {to} is {randint(250,5500)} ")

t=Train(12321)
t.book("Anand","Delhi")
t.getstatus()
t.getfare("Anand","Delhi")