# Query
from sqlalchemy import create_engine, text, inspect
import pandas as pd

engine = create_engine('sqlite:///Chinook.sqlite')

# With context manager
# with engine.connect() as con:
#     rs = con.execute("""SELECT * 
#                             FROM Employee
#                             ORDER BY BirthDate""")
#     df = pd.DataFrame(rs.fetchall())
#     # Set the DataFrame's column names
#     df.columns = rs.keys()

# Pandas way to query
df = pd.read_sql_query("SELECT * FROM Orders", engine)

# Other example
# # Import packages
# from sqlalchemy import create_engine
# import pandas as pd

# # Create engine: engine
# engine = create_engine('sqlite:///Chinook.sqlite')

# # Execute query and store records in DataFrame: df
# df = pd.read_sql_query("SELECT * FROM Album", engine)

# # Print head of DataFrame
# print(df.head())

# # Open engine in context manager and store query result in df1
# with engine.connect() as con:
#     rs = con.execute("SELECT * FROM Album")
#     df1 = pd.DataFrame(rs.fetchall())
#     df1.columns = rs.keys()

# # Confirm that both methods yield the same result
# print(df.equals(df1))

# Other example
# Import packages
from sqlalchemy import create_engine
import pandas as pd

# Create engine: engine
engine = create_engine('sqlite:///Chinook.sqlite')

# Execute query and store records in DataFrame: df
df = pd.read_sql_query("""
    SELECT * 
        FROM Employee
        WHERE EmployeeId >= 6
        ORDER BY BirthDate
""", engine)

# Print head of DataFrame
print(df.head())

# ---------------------------------
# OTHER EXERCISE MEN FROM DATACAMP
# Execute query and store records in DataFrame: df
df = pd.read_sql_query("""
    SELECT *
        FROM PlaylistTrack 
        INNER JOIN Track
            ON PlaylistTrack.TrackId = Track.TrackId
        WHERE Milliseconds < 250000
""", engine)

# Print head of DataFrame
print(df.head())
