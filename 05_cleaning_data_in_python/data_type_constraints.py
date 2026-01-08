# Data science workflow
# Access data -> Explore and process data -> Extract insights -> Report insights 

# Data type constraints
#   - Text data (str)
#       * first name, last name, adress
#   - Integers (int)
#       * number of suscribers, number of products sold
#   - Decimas (float)
#       * Temperature, $ exchange rates 
#   - Binary (bool)
#       * Is married, new customer, yes/no
#   - Dates (datetime)
#       * Order dates, ship dates
#   - Categories (category)
#       * Marriage status, gender 

# Strings to integers
import pandas as pd
# This forces pandas to display all columns
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 1000)

# Import CSV file and output header
sales = pd.read_csv('data//sales.csv')
print(sales.head(2))

# Get data types of columns
print(sales.dtypes)

# Get DataFrame information
# Number of missing values per column
print(sales.info())

# Print sum of all Revenue columns
print(sales['Revenue'].sum())

# Remove $ from Revenue column
sales['Revenue'] = sales['Revenue'].str.strip('$')
# converting revenue column to int
sales['Revenue'] = sales['Revenue'].astype('int')
print(sales['Revenue'])

# ----------------------------------------------------------------------------
# The assert satatement
# Verify that Revenue is now an integer with Assert statement
# assert is a built-in python statement for testing
#   - if the condition is True python does nothing and move to the next line
#   - if the condition is False python crashes with an AssertionError

assert sales['Revenue'].dtype == 'int', "soy JOTO"
# It's true, assert returns nothing
assert 1+1 == 2
# It's false, assert returns AssertionError
# assert 1+1 == 3

# ----------------------------------------------------------------
# Numeric or categorical?
marriage_status = pd.read_csv("data//marriage_status.csv")
print(marriage_status.head(3))
# Categoric 
#   0 -> Never married
#   1 -> Married
#   2 -> Separated
#   3 -> Divorced
print(marriage_status.info())
# Here i can see that the variables are categorical, but in pandas
# detect them as int, so we have to convert them     
print(marriage_status['marriage_status'].describe())

# Convert to categorical
marriage_status["marriage_status"] = marriage_status["marriage_status"].astype('category')
print(marriage_status.info())
print(marriage_status["marriage_status"].describe())

# ------------------------------ DATACAMP EXERCISES ----------------------------------
# 1. Numeric data or ... ?
ride_sharing = pd.read_csv("data//ride_sharing_new.csv")
#   - Print the information of ride_sharing.
print(ride_sharing.info())

#   - Use .describe() to print the summary statistics of the 
#       user_type column from ride_sharing.
print(ride_sharing['user_type'].describe())

#   - Convert user_type into categorical by assigning it the 'category' 
#       data type and store it in the user_type_cat column.
ride_sharing['user_type_cat'] = ride_sharing['user_type'].astype("category")

#   - Make sure you converted user_type_cat correctly by using an assert 
#       statement.
assert ride_sharing['user_type_cat'].dtype == 'category', 'It\'s not a category variable'
print(ride_sharing.head(3))

# ----------------------------------------------------------------------
# 2. Summing strings and concatenating numbers
print(ride_sharing.head(3))

#   - Use the .strip() method to strip duration of "minutes" 
#       and store it in the duration_trim column.
ride_sharing["duration_trim"] = ride_sharing["duration"].str.strip("minutes")
print(ride_sharing.head(3))

#   - Convert duration_trim to int and store it in the duration_time column.
ride_sharing["duration_time"] = ride_sharing["duration_trim"].astype("int")

# Write an assert statement that checks if duration_time's data type is now an int.
assert ride_sharing["duration_time"].dtype == "int", "it's not an int variable"
print(ride_sharing.info())

print(ride_sharing["duration_time"])

# Print the average ride duration.
print(ride_sharing["duration_time"].mean())


