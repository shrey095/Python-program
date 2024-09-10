import os

# Get the current working directory
current_directory = '/C'

# List all files and directories in the current directory
contents = os.listdir(current_directory)

# Print the contents
for item in contents:
 print(item)
