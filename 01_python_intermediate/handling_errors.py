# What is an error?
#   - Code that violates a rule
#   - Error = Exception
#   - Cause our program to terminate !

# COMMON ERRORS
#   - TypeError
#       * Incopatible data type ("Hello" + 5)
#   - ValueError
#       * The value is not within an accepatble range (float("Hello"))

# Note: Error outputs mentions the word "Traceback"
# A traceback can be thought of as a report providing information
# inluding what kind of error ocurred

# ERROR IN PACKAGES
#   - Packages contain other people's code, e.g., custom functions
#   - Known as source code
#   - pip install <package> downloads source code our to our local environment
#   - The pandas pd.read_csv() function executes the code written for that custom function
#       behind the scenes

# Tracebacks from packages
# import pandas as pd
# products = pd.DataFrame({"ID": "ABC1",
#                       "price": 29.99})
# Try to access the non-existent "tag" column
# products["tag"]

# except, raise
# Try to anticipate how errors might occur

# Design-thinking
#    - How might people use our custom function?
#    - Text different approaches
#    - Find what errors might occur

# Error handling in custom functions

# STARTED FUNCTION
def average(values):
    average_value = sum(values) / len(values)
    return average_value

# Where might they go wrong?
#   - average() expexts a list or set
#   - Provide more than one argument
#   - Use the wrong data type

# Providing a dictionary
sales_dict = {"cust_id": ["JL93", "MT12", "IY64"],
              "order_value": [43.21, 68.70, 82.19]}

# Try-except
#   - Avoid error being produced
#   - Still execute subsequent code
def average(values):
    try:
        # Code that might cause an error
        average_value = sum(values) / len(values)
        return average_value
    except:
        # Code to run if an error occurs
        print("average() accpets a list or set. Please provide a correct data type.")

# Raise
#   - Will produce an error
#   - Avoid executing subsequent code
def average(values):
    # CHeck data type
    if type(values) in (list, set):
        # Run if appropiate data type was used
        average_value = sum(values) / len(values)
        return average_value
    else:
        # Run if an Exception occurs
        raise TypeError("average() accepts a list or set, please provide a correct data type.")
    
