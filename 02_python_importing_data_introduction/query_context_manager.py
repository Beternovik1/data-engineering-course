from sqlalchemy import create_engine, text, inspect
import pandas as pd
# Create the engine
engine = create_engine('sqlite:///Northwind.sqlite')
# Create the inspector
inspector = inspect(engine)
# Getting the columns of an specific table
columns = inspector.get_columns('Orders')

for col in columns:
    print(col['name'])

with engine.connect() as con:
    rs = con.execute(text("SELECT OrderID, OrderDate, ShipName From Orders"))
    # import 5 rows
    df = pd.DataFrame(rs.fetchmany(size=5))
    df.columns = rs.keys()
    print(df.head())

# Another example
# Create engine: engine
engine = create_engine('sqlite:///Chinook.sqlite')

# Open engine in context manager
with engine.connect() as con:
    rs = con.execute("""SELECT * 
                            FROM Employee
                            ORDER BY BirthDate""")
    df = pd.DataFrame(rs.fetchall())

    # Set the DataFrame's column names
    df.columns = rs.keys()

# Print head of DataFrame
print(df.head())

# ----------------------------------------
# OTHER EXAMPLE FROM DATACAMP
# Open engine in context manager
# Perform query and save results to DataFrame: df
with engine.connect() as con:
    rs = con.execute("""
        SELECT Title, Name
            FROM Album
            INNER JOIN Artist
                ON Album.ArtistID = Artist.ArtistID
    """)
    df = pd.DataFrame(rs.fetchall())
    df.columns = rs.keys()

# Print head of DataFrame df
print(df.head())
