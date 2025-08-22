import os

# Get current working directory
current_directory = os.getcwd()

# Print the current directory path
print("Current Directory:", current_directory)

# List and print all files and directories in the current directory
contents = os.listdir('/New folder')
print("'/new folder:")
for item in contents:
    print(item)
