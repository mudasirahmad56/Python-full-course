import os

# Select the current_directory you want to list
current_directory = os.getcwd()
print("Current Directory:", current_directory)
# use os to list files in the current_directory
contents = os.listdir(current_directory)
print("\nContents of the directory:")
for item in contents:
    print(item)
