# Basic SQL query 
# SELECT * FROM Table_Name
# Returns all columns of all rows of the table

# Workflow of SQL querying
#   - Import packages and functions
#   - Create the engine
#   - Connect to the engine
#   - Query the database
#   - Save query results to a DataFrame
#   - Close the connection

from sqlalchemy import create_engine, text
import pandas as pd
# Create the engine
engine = create_engine('sqlite:///Northwind.sqlite')

# Connect using the ENGINE
con = engine.connect()

# Query the DB
rs = con.execute(text("SELECT * FROM Orders"))
# Turning the of rs into a dataframe
df = pd.DataFrame(rs.fetchall())
df.columns = rs.keys()
# Close the connection
con.close()
print(df.head())


