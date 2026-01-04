# API
#   - Application Programming Interface
#   - Protocols and routines 
#       * Building and interacting with software applications

# A standard for transferring data through API's is:
# JSONs
#   - JavaScript Object Notation
#   - Real-time server-to-browser communication
#   - Douglas Crockford
#   - Human readable
# They keys in JSONS will always be strings enclosed in quotation marks (parentesis)
# The values can be strings, integers, arrays or even objects

# Loading JSONs with python in the working directory
import json
with open('snakes.json', 'r') as json_file:
    # Loading the json file as a dictionary
    json_data = json.load(json_file)

print(type(json_data))
# Printing the key value to the console
for key, value in json_data.items():
    print(key + ':', value)

# ------------------------
print("-------------------Exercise from Datacamp--------------------")
# Load JSON: json_data
with open("a_movie.json") as json_file:
    json_data = json.load(json_file)

# Print each key-value pair in json_data
for k in json_data.keys():
    print(f'\"{k}\": \"{json_data[k]}\",')