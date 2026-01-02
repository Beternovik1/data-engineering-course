# Reading a text file
filename = 'huck_finn.txt'
file = open(filename, mode='r') # r is to read
text = file.read()
# IS IMPORTANT TO ALWAYS CLOSE THE CONNECTION TO THE FILE
file.close()
print(text)

# Writing to a file
# Python wipes the file to prepare for new content
# filename = 'huck_finn.txt'
# file = open(filename, mode='w') # w is to write
# file.close()

# Context manager with (to avoid having to close the connection to the file)
with open('huck_finn.txt', 'r') as file:
    print(file.read())

# -----------------------------------------

# Flat files