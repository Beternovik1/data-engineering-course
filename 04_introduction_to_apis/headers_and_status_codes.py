# Request and response message anatomy
# What if you wnat to give the server extra instructions?
# or check that the server properly handled our request?
# -----------------------------------------------
# Request message
# - response line
#       * GET /users/42 HTTP/1.1 (request line)
# - headers
#       * Host: datacamp.com
#       * Accept: application.json
# Body: Empty

# ----------------------------------------------
# Response message 
# - response line
#       * HTTP/1.1 200 OK 
# - headers
#       * Content-Type: application/json
#       * Content-Language: en-US
#       * Last-Modified: Wed, 21 Oct 2023 07:28:00 GMT
# - body
# {
#   "id": 42,
#   "name": "John Doe",
#   "age": 30,
#   "email": "john@datacamp.com" 
# }

# The start-line
#   - Request messages: Is referred as the request-line, it contains the 
#   request type such as 'GET' or 'POST', along with the path where
#   the message should be delivered to 
#       * GET /users/42 HTTP/1.1 (request line)

#   - Response messages: Is referred as status-line, it contains a three-digit
#   numerical status-code and a status message
#       * HTTP/1.1 200 OK 

# Note: A server will always include a numeric status code in the 
# response message 

# Status codes
#   - Status code categories
#       * 1XX: Informational responses
#       * 2XX: Successful responses
#       * 3XX: Redirection messages
#       * 4XX: Client error responses
#       * 5XX: Server error responses

# Frequently used status codes
#   - 200: OK (indicates the server has correctly processed the request)
#   - 404: NotFound (indicates that the resorce we are requesting doen't exist)
#   - 500: Internal Server Error (an error has ocurred on the server)

# Headers
#   - Contain information that describe the message or data being sent
#   or received, such as the type of content we're sending or the date 
#   the requested resource was last modified.
#   - Headers are always formatted as key-value pairs separated by a colon 
#       * key1: Value 1
#       * key3: Value 2
#   - In order to effectively communicate, client and server use message
#   headers to agree on the language they are using to exchange information
#   this is called 'Content negotiation'
#       * Client adds an accept: application/json header to the request
#       * Server responds with a content-type: application/json header 
 
# The response object has a header attribute, wich is a dictionary 
# containing one key-value pair for every header received back in the response
# Adding headers to a request
import requests
response = requests.get(
    'https://api.datacamp.com',
    headers={'accept':'application/json'}
)
# Reading response headers
# Form 1: Subsetting the dictionary using square brackets
print(response.headers['content-type'])  
# Form 2: Using the .get() method on the dictionary
print(response.headers.get('content-type'))

# Status codes with requests
response = requests.get('https://apid.datacamp.com/users/12')
# Seeing if the status_code is 404?
print(response.status_code == 404)
# Looking up status codes using requests.codes
response = requests.get('https://api.datacamp.com/this/is/the/wrong/path')
# Looking up if status code is 404?
print(response.status_code == requests.codes.not_found)


# ------------------------------------------------------
# Exercises from datacamp
# Make a request to the movies endpoint of the API
response = requests.get('http://localhost:3000/movies')

if (response.status_code == 200):
  print('The server responded succesfully!')
  
# Check the response status code
elif (response.status_code == 404):
  print('Oops, that API could not be found!')

# ----------------------------------------------
response = requests.get('http://localhost:3000/movies')

# Check if the response.status_code is equal to the requests.codes value for "200 OK"
if (response.status_code == requests.codes.ok):
  print('The server responded succesfully!')
  
# Or if the request was not successful because the API did not exist
elif (response.status_code == requests.codes.not_found):
  print('Oops, that API could not be found!')

# --------------------------------------------------------
# Find out the content-type of the response by printing out the 
# response content-type header.
response = requests.get('http://localhost:3000/lyrics')

# Print the response content-type header
print(response.headers['content-type'])

# Find out what content-types the server can respond with by printing 
# out the response accept header.
response = requests.get('http://localhost:3000/lyrics')

# Print the response accept header
print(response.headers.get('accept'))

# Add an accept header to the request so the server returns JSON 
# formatted data, then print the response text attribute.
# Set the content type to application/json
headers = {'accept': 'application/json'}
response = requests.get('http://localhost:3000/lyrics', headers=headers)

# Print the response's text
print(response.text)


# Add an accept header to request a response in the application/xml
# content-type from the server.
# Check if the server did not accept the request using the relevant 
# status code.
# Print out a list of accepted content types from the server response.
# Add a header to use in the request
headers = {'accept': 'application/xml'}
response = requests.get('http://localhost:3000/lyrics', headers=headers)

# Check if the server did not accept the request
if (response.status_code == 406):
  print('The server can not respond in XML')
  
  # Print the accepted content types
  print('These are the content types the server accepts: ' + response.headers['accept'])
else:
  print(response.text)