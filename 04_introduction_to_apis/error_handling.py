# Error status codes 
# A status code in the 4XX(400) or 5XX(500) indicates an issue

#   - 4XX Client Errors
#       * Indicate issues on the client's end
#       * Common causes: Bad requests, authentication failures, etc...
#       * Resolution: Fix the request 
#       * Common 4XX errors:
#           -> 401 Unauthorized - The request lacks valid authentication
#               credentials for the requested resource
#           -> 404 Not Found - Indicates that the server cannot find 
#               the resource that was requested
#           -> 429 Too Many Requests - The cliet has sent too many 
#               requests in a given amount of time
#   - 5XX Server Errors
#       * Arises from problems on the server
#       * Common causes: Server overloaded, server configuration
#         errors, internal errors
#       * Resolution: Should be fixed by the API administrator
#       * Common 5XX errors
#           -> 500 Internal Server Error - The server experienced an 
#               unexpected issue which prevents it from responding
#           -> 502 Bad Gateway - The API server could not successfully 
#               reach another server it needed to complete the response 
#           -> 504 Gateway Timeout - The server (which acts as a gateway)
#               did not get a resopnse from the upstream server in time

# Handling errors 
# The simplest way to handle API errors is by checking the response status code
# for any codes in the 400 and 500 range, which indicate an error has occurred

# API errors
import requests
url = 'http://api.music-catalog.com/albums'
r = requests.get(url)
if r.status_code >= 400:
    print("Oops, something went wrong ")
else:
    print("All fine, let's do something with the response")

# Connection errors
# An error might occur even befor the request reaches the server,
# in this case we would not receive a response containing an error code.
# Fortunately, the requests library raises a ConectionError 
import requests
from requests.exceptions import ConnectionError
url = ''

try:
    r = requests.get(url)
    print(r.status_code)
except ConnectionError as conn_err:
    print(f'Connection Error! {conn_err}.')

# raise_for_status()
# requests library contains a feature that automatically raises errors for 
# any responses containing an error status code. With raise_fro_status()
# function inmediately after sending the request any error code returned
# from the API will raise an 'HTTPError'. This way, after checking for 
# connection errors, we can easily also check for any HTTPErrors that 
# might have occurred
import requests
# 1: Import the requests library exeptions
from requests.exceptions import ConnectionError, HTTPError

try: 
    r = requests.get("http://api.music-catalog.com/algums")

    # 2: Enable raising exceptions for returned error statuscodes
    r.raise_for_status()
    print(r.status_code)

# 3. Catch any connection errors
except ConnectionError as conn_err:
    print(f'Connection Error! {conn_err}.')
 

# ---------------------------- DATACAMP EXERCISES -------------------------------
# 1. Handling errors with Requests
#   - Import the exception class used to detect connection errors from the requests package, 
#       then use the imported class to intercept the error raised by the API request.
# Import the correct exception class
from requests.exceptions import ConnectionError

url ="http://wronghost:3000/albums"
try: 
    r = requests.get(url) 
    print(r.status_code)
# Use the imported class to intercept the connection error
except ConnectionError as conn_err: 
    print(f'Connection Error! {conn_err}.')


#   - Import the exception class used to detect errors returned via the response status code,
#        then enable the setting on the response object which will automatically raise an error 
#       when an unsuccessful status code value is received. Finally, intercept the imported 
#       exception to print an error.


