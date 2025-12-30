# Creating a custon function to calculate the average value
def average(values):
    # Calculate the average
    return round(sum(values) / len(values), 2)

# List of preparation times (minutes)
preparation_times = [19.23, 15.67, 48.57, 23.45, 12.06, 34.56, 45.67]

# Calculating the average
print(average(preparation_times))
average_time = average(preparation_times)
print(average_time)

# Values = Argument

# Arguments
#   - Values provided to a function or method, two types:
#       * Positional arguments: Provide arguments in order, separated by commas
#           E.g. Round pi to 2 digits
#           print(round(3.1415926535, 2))

#       * Keyword: Provide arguments by assigning values to keywords, useful for
#         for interpretation and tracking arguments
#           E.g. Round pi to 2 digits
#           print(round(number=3.1415926535, ndigits=2))

# Identifying keyword arguments with help functions 
# print(help(round))
'''
Help on built-in function round in module builtins:

round(number, ndigits=None)
    Round a number to a given precision in decimal digits.

    The return value is an integer if ndigits is omitted or None.  Otherwise
    the return value has the same type as the number.  ndigits may be negative.

'''
# - None = no value/empty
# - Default argument: way of setting a default value for an argument
# - We overwrite None to 2

# Adding an argument to our custon function
def average(values, rounded=False):
    # Round avergate to two decimal places if rounded is True
    if rounded == True:
        return round(sum(values) / len(values), 2)
    # Otherwise, don't round
    else:
        return sum(values) / len(values)
    
# Get the average without rounding
print(average(preparation_times))
# Get the rounded average
print(average(preparation_times, rounded=True))

# Docstring
#   - String (block of text) describing a function

# Access only the docstring
# .__doc__: "dunder-doc" attribute
print(round.__doc__)

# Creating a docstring
def average(values):
    # One-line docstring
    """Find the mean in a sequence of values and round to two decimal places."""
    return round(sum(values) / len(values), 2)

# Access our docstring
print(average.__doc__) 

# Updating a function's docstring
average.__doc__ = "Calculate the mean of values in a data structure, rounding the results to 2 digists"
print(help(average))

# Multi-line docstring
def average(values):
    """
    Find the mean in a sequence of values and round to two decimal places.
    
    Args:
        values(list): A list of numeric values.
        
    Returns:
        rounded_average (float): The mean of values, rounded to two decimal places.
    """
    return round(sum(values) / len(values), 2)
# Accessing the docstring with help
print(help(average))

# Arbitrary positional arguments
#   - Docstrings help clarify how to use suctom functions
#   - Arbitrary arguments allow functions to accept any number of arguments
#   - Conventional naming: *args
#   - Allows a variety of uses while producing expected results !

# Allow any number of positional, non-keyword arguments
def average(*args):
    # One-line docstring
    """Find the mean in a sequence of values and round to two decimal places."""
    return round(sum(args) / len(args), 2)

# Using arbitrary positional arguments
# calling average with wix positional arguments
print(average(15, 29, 4, 13, 11, 8))

# Args create a single iterable
#   - *: Convert arguments to a single iterable (tuple)
print(average(*[15, 29], *[4, 13], *[11, 8]))

# Arbitrary keyword arguments: **kwargs
#   - keyword = value
# Use arbitrary keyword arguments
def average(**kwargs):
    return round(sum(kwargs.values()) / len(kwargs.values()), 2)

# Using arbitrary keyword arguments
# Calling average with six kwargs
print(average(a=15, b=29, c=4, d=13, e=11, f=8))

# Calling average with one kwargs
print(average(**{"a":15, "b":29, "c":4, "d":13, "e":11, "f":8}))
# Each key-value pair in the dictionary is mapped to a keyword argument and value !

# Calling average with three kwargs
print(average(**{"a":15, "b":29}, **{"c":4, "d":13}, **{"e":11, "f":8}))
