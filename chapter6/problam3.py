# Write a program to find out whether a student has passed or failed if it requires a 
# total of 40% and at least 33% in each subject to pass. Assume 3 subjects and 
# take marks as an input from the user. 

sub1=float(input("Enter the Subject 1 marks : "))
sub2=float(input("Enter the Subject 2 marks : "))
sub3=float(input("Enter the Subject 3 marks : "))

total_percentage=(100*(sub1+sub2+sub3))/300
# total_percentage=(sub1+sub2+sub3)/3
if(total_percentage>=40 and sub1>=33 and sub2>=33 and sub3>=33):
    print("Your are pass and your percentage = ",total_percentage)
else:
    print("Your are fail and your percentage = ",total_percentage)