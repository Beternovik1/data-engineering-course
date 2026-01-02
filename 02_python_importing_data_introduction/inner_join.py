from sqlalchemy import create_engine, inspect
import pandas as pd
engine = create_engine('sqlite:///Northwind.sqlite')
inspector = inspect(engine)
print("----- TABLE NAMES -----")
tables = inspector.get_table_names()
print(tables)

print("---- COLUMNS FROM \"ORDERS\" TABLE -----")
columns_orders = inspector.get_columns('Orders')
for col in columns_orders:
    print(col['name'])

print("----- COLUMNS FORM \"CUSTOMERS\" TABLE")
columns_custumers = inspector.get_columns('Customers')
for col in columns_custumers:
    print(col['name'])


# -------- QUERY WITH JOIN ------------
df = pd.read_sql_query("""
    SELECT OrderID, CompanyName 
        FROM Orders
        INNER JOIN Customers
            ON Orders.CustomerID = Customers.CustomerID
""", engine)
print(df.head())