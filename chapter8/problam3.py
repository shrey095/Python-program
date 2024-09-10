#  Write a python program using function to convert Celsius to Fahrenheit. 
'''
Convert Celsius to Fahrenheit using the °F = (°C x 1.8) + 32 or °F = (°C x 9/5) + 32
Convert Fahrenheit to Celsius with the °C = (°F - 32) x 5/9
'''
c=float(input("Enter the value of Celsius = "))

def con():
    f=(c*1.8)+32
    print("The value of Fahrenheit = ",f)
    # print(f"{round(f,2)}°F")

con()

'''
exter 
f=float(input("Enter the value of Fahrenheit = "))
   
def con():
    c=(f-32)*(5/9)
    print("The value of Celsius = ",c)

con()

'''