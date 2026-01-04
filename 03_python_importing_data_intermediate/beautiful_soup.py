# HTML
#   - Mix of unstructured and structured data
#   - Structured data:
#       * Has pre-defined data moede, or
#         organized in a defined manner
#   - Unstructured data: neither of these properties

# BeautifulSoup
#   - Parse and extract structured data from HTML
#   - Make tag soup beautiful and extract information

# from bs4 import BeautifulSoup
# import requests
# url = 'https://www.crummy.com/software/BeautifulSoup/'
# r = requests.get(url)
# html_doc = r.text
# soup = BeautifulSoup(html_doc)

# Making html pretty with indentation
# print(soup.prettify())

# Printing tha title of the HTML 
# print(soup.title)

# # Printing each link in the HTML
# for link in soup.find_all('a'):
#     print(link.get('href'))

# ---------------------------------------------
# Example prettifing the html of wikipedia
# Import packages
import requests
from bs4 import BeautifulSoup

# Specify url: url
url = 'https://www.python.org/~guido/'

# Package the request, send the request and catch the response: r
r = requests.get(url)

# Extracts the response as html: html_doc
html_doc = r.text

# Create a BeautifulSoup object from the HTML: soup
soup = BeautifulSoup(html_doc)

# Prettify the BeautifulSoup object: pretty_soup
pretty_soup = soup.prettify()

# Print the response
print(pretty_soup)

# Get the title of Guido's webpage: guido_title
guido_title = soup.title

# Print the title of Guido's webpage to the shell
print(guido_title)

# Get Guido's text: guido_text
guido_text = soup.text

# Print Guido's text to the shell
print(guido_text)

# Find all 'a' tags (which define hyperlinks): a_tags
a_tags = soup.find_all('a')

# Print the URLs to the shell
for link in a_tags:
    print(link.get('href'))