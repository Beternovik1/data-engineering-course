# What are URLs?
#   - URL = Uniform Resource Locator
#   - The structured address to an API Resource
#   - Customize the URL to interacto with specific API Resources

# Disecting the URL
# http://350.5th-ave.com:80/unit/243?floor=77

# http://       350.5th-ave.com     :80       /unit/243         ?floor=77
# Protocol          Domain          Port        Path              Query

#   - Protocol = the means of transportation (e.g. Walking or driving)
#   - Domain = the street address of the office building (uniquely identifies
#               the location of the API server on the internet)
#   - Port = the gate or door to use when enterint the building (e.g. when 
#               traveling by car, we enter though the garage)
#   - Path = the specific office unit inside the building (each resources
#               has a unique location on the server, defined by its path)
#   - Query = any additional instructions (e.g. "Take the elevator")

# By constructing a URL with a path and parameters, we can control where to send
# our API requests to. 

# -------- Adding query parameters with requests -----------
# 'http://350.5th-ave.com/unit/243' this is the direction of an specific datacamp office

import requests
# Append the query parameter to the URL string
response = requests.get('http://350.5th-ave.com/unit/243?floor=77&elevator=True')
print(response.url)

# Use the params argument to add query parameters
# Create dictionary
query_params = {'floor':77, 'elevator':True}
# Pass the dictionary using the params argument
response = requests.get('http://350.5th-ave.com/unit/243', params=query_params)
print(response.url)

# ------------------------------------------------------
# --- Sending a package to the DataCamp office ---------

# HTTP VERBS
#   - Destination: Unit 243 of the 350 5th Ave office building
#   - URL: http://350.5th-ave.com/unit/243
# ----------------------------------------------------------------
#                   ACTIONS
# ----------------------------------------------------------------
# Verb          Action           Description
# ----------------------------------------------------------------
# GET           Read             Check the mailbox contents
# POST          Create           Drop a new package in the mailbox
# PUT           Update           Replace all packages with a new one
# DELETE        Delete           Remove all packages from the mailbox

# Sending data via POST and PUT
#   - Each verb has it's own method in the requests package
#   - use the data argument to pass data to a POST or PUT request.

# GET = Retrieve a resource 
response = requests.get('http://350.5th-ave.com/unit/243')

# POST = Create a resource
response = requests.post('http://350.5th-ave.com/unit/243', data={"key": "value"})

# PUT = Update an existing resource
response = requests.put('http://350.5th-ave.com/unit/243', data={"key": "value"})

# DELETE = Remove a resource
response = requests.delete('http://350.5th-ave.com/unit/243')


