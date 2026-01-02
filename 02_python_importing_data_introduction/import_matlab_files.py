# MATLAB
#   - "Matrix Laboratory"
#   - Industry standard in engineering and science
#   - Data saved as .mat files

# Scipy 
#   - scipy.io.loadmat() - read .mat files
#   - scipy.io.savemat() - write .mat files

# Importing a .mat file
# The library converts the MATLAB file into a python dictiony
# where each MATLAB variable is a KEY and the value of the variable
# is the value of the KEY
import scipy.io
filename = 'workspace.mat'
mat = scipy.io.loadmat(filename)
print(type(mat))

# keys = MATLAB variable names
# values = objects assigned to variables
print(type(mat['x']))
