#  Write a program to mine a log file and find out whether it contains ‘python’. 

# with open("log.txt","r") as f:
#     content=f.read()
# if("python" in content):
#     print("Yes Python is Present")
# else:
#     print("No Python is not Present")


    # Write a program to find out the line number where python is present from ques 6. 
with open("log.txt","r") as f:
    lines=f.readlines()
    
lineno=1
for line in lines:
    if("python" in line):
        print(f"Yes Python is Present.Line no = {lineno}")
        break
    lineno += 1
else:
     print("No Python is not Present")
