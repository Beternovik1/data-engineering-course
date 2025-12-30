# Modules are Python scripts (files ending with .py)
#   - containg ructions and attributes
#   - can contain other modules
#   - can contain other modules
# Help us avoid rewriting code that already exists !
# There are around 200 built-in modules 

# OS:
#   - Used for interacting with our operating system
#   - Check the current directory
#   - List available files
#   - Access environment variables

# STRING: 
#   - Simplifies text processing tasks

# Importing a module 
#   General syntax
# import <module_name>

# Importing the os module
import os
print(type(os))

# Finding a module's functions
#   - Check the documentation
# Call help()
# Warning - will return a very large output!
# print(help(os))

# Getting the current working directory
# Using an os funciton
print(os.getcwd())

# Useful if we need to reference the directory later
# Assign to a variable
work_dir = os.getcwd()

# Changing directory 
os.chdir("C:\\Users\\ASUS\\Documents\\cursos\\data-engineering-course")

# Check the current directory 
print(os.getcwd())

# Changing to the other directory 
os.chdir("C:\\Users\\ASUS\\Documents\\cursos\\data-engineering-course\\01_python_intermediate")
print(os.getcwd())

# Module attributes
#   - Attributes return values
#   - Functions perform tasks
#   - Don't use parenteses with attributes
# Get the local envionment
# print(os.environ)

# String module
#   - contains letters, numbers, or specific characters
#   - Handy for validating user input
import string

# This returns all lower case letters
print(string.ascii_lowercase)
# This returns numbers to 0 to 9
print(string.digits)
# This returns all putntuation symbols
print(string.punctuation)


