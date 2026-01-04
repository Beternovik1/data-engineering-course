# What is an API?
#   - Application Programming Interface
#   - Set of communication rules and abilities

# Web APIs, clients and servers
#   - Web APIs communicate over the internet using HTTP
#   - Client setnds a request message to a Server
#   - Server returns a response message to the Client

# Types of Web APIs
#   - SOAP
#       * Focus on strict and formal API design 
#       * Enterprise applications
#   - REST
#       * Focus on simplicity and scalability
#       * Most common API architecture
#   - GraphQL
#       * Focus on flexibility
#       * Optimized for performance 
# 
# In the course i am going to use just REST APIs

# Working with APIs in Python
from urllib.request import urlopen
import requests
api = "http://api.music-catalog.com/"

#   - urlib
#       * Bundled with python
#       * Powerful but not very developer-friendly
# urlopen function to send the request
with urlopen(api) as response:
    # read() funciton to get the response data
    data = response.read()
    # decode() function to extract the raw data
    string = data.decode()
    print(string)

#    - requests (simplifies things a lot)
#       * Many powerful built-in features
#       * Easier to use
# requests takes care of reading and decoding the response just by 
# printing the text attribute of the response object 
response = requests.get(api)
print(response.text)
