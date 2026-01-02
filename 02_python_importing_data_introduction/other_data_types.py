# Other file types
#   - Excel spreadsheets
#   - SAS files
#   - Stata files
#   - HDF5 files 
#   - Pickeled file
#       * File type native to Python
#       * Motivation: many datatypes for whitch it isn't
#         obvious how ot store them
#       * Pickled files are serialized
#       * Serialize = convert object to bytestream

# PICKLE
import pickle
# rb -> to specify read only and binary 
with open('piclked_fruit.pkl', 'rb') as file:
    data = pickle.load(file)
print(data)

# EXCEL 
import pandas as pd
file = 'urbanpop.xlsx'
data = pd.ExcelFile(file)
print(data.sheet_names)
df1 = data.parse('1960-1966') # sheet name, as a string
df2 = data.parse(0) # sheet index, as a float