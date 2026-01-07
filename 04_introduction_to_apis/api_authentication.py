# APIs we interact with frequently contain private, personal or sensitive data
# To protect this sensitive information, APIs require clients to authenticate 
# before granting access

# --------------- Authentication methods ------------------------
# Basic autentication
#   - Simplest form of API authentication
#   - It uses a username and password for authentication
#   - Is easy to integrate but also the least secure as it 
#     sends your password unencrypted over the internet to the server
# API key/token Authentication
#   - Works by attaching a unique authentication key or token to each request
#   - API keys are simple to implement but pose a security risk if compromised, 
#     as they also transmit unencrypted data
# JWT Authentication (JSON Web Token Authentication) 
#   - Is similar to API key authentication, but the main difference is that
#     JWT token has a limited lifespan and can contain additional encrypted
#     data, such as user information
# OAuth 2.0 
#   - Is a comprehensive authentication framework that allows fine-graned
#     access to resources without sharing any credentials 

# Note: Check the documentation of the API you are using to learn which 
# method to use for authentication 

# Basic authentication with request package
#   - We need to add an authorization header to the request we are sending
#     the API
#   - request line
#       * GET /users/42 HTTP/1.1
#   - headers
#       * Host: datacamp.com
#       * Accept: application/json
#       * Authorization: Basic dXNlcjpwYXNzd29yZA= 
#          This header must contain a base64-encoded combination of our username
#          and password. Base64 encoding is a two-way algorithm easy to decode

# This will automatically add a Basic Atuthetication header before sending
# the request
import requests
requests.get('http://api.music-catalog.com', auth=('username', 'password'))

# API key/token authentication 
#   - First option: Adding the API key to the URL as a query parameter
params = {'access_token': 'faaa1c97bd3f4bd9b024c708c979feca'}
requests.get('http://api.music-catalog.com/albums', params=params)
# url = http://api.music-catalog.com/albums?access_token=faaa1c97bd3f4bd9b024c708c979feca

#   - Second option: Using the "Bearer" authorization header (prefered method)
headers = {'Authorization': 'Bearer faaa1c97bd3f4bd9b024c708c979feca'}
requests.get('http://api.music-catalog.com/albums', headers=headers)

# -------------------------------------------------------------------
# ------------------- DATA CAMP EXERCISES ---------------------------

# Basic Authentication with requests
#   - Check the numeric status code value on the request object for a successful
#       response.
#   - Also check for a failed authentication request which has a specific 
#       status-code too.
#   - Create the correct authentication variable with your username and password.
#   - Then pass the authentication variable to the requests.get() method 
#       using the correct argument.
# Create the authentication tuple with the correct values for basic authentication
authentication = ('john@doe.com', 'Warp_ExtrapolationsForfeited2')

# Use the correct function argument to pass the authentication tuple to the API
response = requests.get('http://localhost:3000/albums', auth=authentication)

if(response.status_code == 200):
    print("Success!")
elif(response.status_code == 401):
    print('Authentication failed')
else:
    print('Another error occurred')

# API key authentication with requests
'''
1. Create a dictionary with a key-value pair for the API key. 
The API expects the access_token URL parameter to contain 
your unique API key.
Pass the dictionary to the requests.get() function 
using the correct argument to pass URL parameters.
'''
# Create a dictionary containing the API key using the correct key-value combination
params = {'access_token': '8apDFHaNJMxy8Kt818aa6b4a0ed0514b5d3'}
# Add the dictionary to the requests.get() call using the correct function argument
response = requests.get('http://localhost:3000/albums', params=params)

if(response.status_code == 200):
    print("Success!")
elif(response.status_code == 401):
    print('Authentication failed')
else:
    print('Another error occurred')

'''
2. Create a dictionary that includes a key-value pair for the API key,
 this time using the Authorization header.
Pass the dictionary to the requests.get() function
 as headers.
'''
# Create a headers dictionary containing and set the API key using the correct key and value 
headers = {'Authorization': 'Bearer 8apDFHaNJMxy8Kt818aa6b4a0ed0514b5d3'}
# Add the headers dictionary to the requests.get() call using the correct function argument
response = requests.get('http://localhost:3000/albums', headers=headers)

if(response.status_code == 200):
    print("Success!")
elif(response.status_code == 401):
    print('Authentication failed')
else:
    print('Another error occurred')