# Simple functions
def average(values):
    average_value = sum(values) /len(values)
    return average_value

# Lambda functions
#   - lambda keyword
#       * Represents an anonymous function
# General syntax
# lambda arguments:expression
#   - Convention is to use x for a single argument
#   - The expression is the equivalent fo the function body
#   - No return statement is required
#   - Can be stored as a variable

# Lambda average function
# The output shows that a lambda function was created 
print(lambda x: sum(x) / len(x))

# Custum average function
def average(x):
    return sum(x) / len(x)
print(average)

# Get the average with lambda
print((lambda x: sum(x) / len(x))([3, 6, 9])) 

# Store lambda function as a variable
average = lambda x: sum(x) / len(x)
# Call the average function
print(average([3, 6, 9]))

# Lambda funciton with two arguments
power = lambda x, y: x**y
# Raise 2 to the poser of 3
print(power(2, 3)) 

# Lambda funcitons with iterables
#   - map() applies a function to all elements in an iterable
names = ["john", "sally", "leah "]
# Apply a lambda function inside map()
# The method capitalize() is used to format a string so that the 
# frist character is converted to uppercase and all the other characters
# are converted to lowercase
capitalize = map(lambda x: x.capitalize(), names)
# It outputs a map object pointing to the memory location where this function
# is stored
print(capitalize)
# To produce an output we need to convert it to a datastructure
# Convert to a list
print(list(capitalize))

# When to use lambda or custom functions
# Scenario                  Function Type
# Complex task                  Custom
# Same task several times       Custom
# Performed once                Lambda
# Simple task                   Lambda
