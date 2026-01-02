# Creating a database engine
#   - SQLite database
#       * Fast and simple
#   - SQLAlchemy
#       * Workds with many Relational Database Mnagement Systems

# Importing the library
# $ python -m pip install h5py
from sqlalchemy import create_engine, inspect
# Create the engine
engine = create_engine('sqlite:///Northwind.sqlite')

# Create the inspector to know what tables exists
inspector = inspect(engine)

# Getting table names
table_names = inspector.get_table_names()
print(table_names)

