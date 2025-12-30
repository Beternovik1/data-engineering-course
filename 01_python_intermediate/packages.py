# PACKAGES
# * A collection of modules = Package
#   - Also called a library
# * Publicly available and free
# * Downloaded from PyPI
# * Then can be imported and used like modules

# Installing a package
#  * Terminal / Command Prompt
#       python3 -m pip install <package_name>
#  * python3 executes Python code from the terminal
#  * pip preferred installer 

# Installing pandas
# * A package for data manipulation and analysis 
#       python3 -m pip install pandas 

# Import pandas using an alias
import pandas as pd

# Sales dictionary
sales = {
    "user_id":["KM37", "PR19", "YU99"],
    "order_value":[197.75, 208.21, 134.99]
}

# Convert to a pandas DataFrame
sales_df = pd.DataFrame(sales)
print(sales_df)

# Saving the datafram in a csv in our current directory
# index=False add a new column for the row numbers (0,1,2...)
sales_df.to_csv('sales.csv', index=False)

# Reading in a CSV file in our current directory
sales_df = pd.read_csv("sales.csv")

# Checking the data type
print(type(sales_df))  

# Previewing the file (first 5 rows displayed)
print(sales_df.head())

# Chedking the file info
print(sales_df.info()) 

# Functions versus methods
#   - Function = code to perform a task
#       * e.g. A built-in function, a pandas function
#   - Method = a function that is specific to a data type 
