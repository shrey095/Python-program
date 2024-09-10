# A spam comment is defined as a text containing following keywords: 
# “Make a lot of money”, “buy now”, “subscribe this”, “click this”. Write a program 
# to detect these spams. 

s1="Make a lot of money"
s2="buy now"
s3="subscribe this"
s4="click this"

massage=input("Enter Your massage : ")
# if((s1=="Make a lot of money") or (s2=="buy now") or (s3=="subscribe this") or (s4=="click this")):
if((s1 in massage) or (s2 in massage) or (s3 in massage) or (s4 in massage)):
    print("It is Spamm massage")
else:
    print("It is not Spamm massage")
