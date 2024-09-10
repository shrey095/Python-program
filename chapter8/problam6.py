# Write a python function which converts inches to cms
'''
1 inch = 2.54 cm

1 cm = 0.3937 inch
'''
def inch_to_cm(inch):
     return inch*2.54
    #  print(f"{i} inches to cms = {i*2.54}cm")

i=float(input("Enter the value in Inch : "))


print(f"{i} inches to cms = {inch_to_cm(i)}cm")
