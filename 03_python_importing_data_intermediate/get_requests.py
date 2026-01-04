# URL
#   - Uniform/Universal Resource Locator
#   - References to web 
#   - Focus: web addresses
#   - Ingredients:
#       * Protocol identifier - http:
#       * Resource name - datacamp.com
#   - These specify web addresses uniquely

# HTTP
#   - HyperText Transfer Protocol
#   - Foundation of data communication for the web
#   - HTTPS - more secure form of HTTP
#   - Going to a website = sending HTTP request
#       - GET request
#   - urlretrieve() performs a GET request
#   - HTML - HyperText Markup Language

# GET requests using urllib
# Extranting the HTML from wikipedia home page
# from urllib.request import urlopen, Request
# url = "https://www.wikipedia.org/"
# request = Request(url)
# response = urlopen(request)
# html = response.read()
# response.close()

# GET requests using requests
# import requests
# url = "https://www.wikipedia.org/"
# r = requests.get(url)
# # text contains the html of wikipedia as a string
# text = r.text
# print(text)

# -------------------------------------------
# Latest update of the datacamp code
import requests
url = "https://www.wikipedia.org/"

# Define the headers to look like a real browser
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}

# Pass the headers to the get() function
r = requests.get(url, headers=headers)

# Now print the text
text = r.text
print(text)
