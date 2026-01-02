# HDF5 files
#   - Hierarchical Data Format version 5
#   - Standard for storing large quantities of numerical data
#   - Datasets can be hundreds of gigabytes or terabytes
#   - HDF5 can scale to exabytes
# Importing HDF5 files
import h5py
import numpy as np
filename = 'H-H1_LOSC_4_V1-815411200-4096.hdf5'
data = h5py.File(filename, 'r') # 'r' is to read
print(type(data))

# The structure of HDF5 files
# for key in data.keys():
#     print(key)

# The structure of HDF5 files
for key in data['meta'].keys():
    print(key)
    

# Printing 
print(np.array(data['meta']['Description']), np.array(data['meta']['GPSstart']))\

