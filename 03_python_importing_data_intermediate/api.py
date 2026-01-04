# What is an API?
#   - Set of protocols and routines
#   - Bunch of code
#       * Allows two software programs to communicate
#       * with each other

# Connecting to an API in Python 
import requests
# Decomposing the URL
#   - http -> making an HTTP request
#   - www.omdbapi.com -> querying the OMDB API
#   - ?t = hackers
#       * The string that begins with question mark is called a Query String
#       * Return data for a movie with title(t) 'hackers'
url = 'http:///www.omdbapi.com/?t=hackers'
# Packaging and sending the request to the URL
r = requests.get(url)
# The response object 'r' has an associate object named json
# this returns a dictionary 
json_data = r.json()
for key, value in json_data.items():
    print(key + ':', value)

# -------------------------
print("--------- Other exercise from DataCamp -----------------")
# Import requests package
import requests

# Assign URL to variable: url
url = 'http://www.omdbapi.com/?apikey=72bc447a&t=the+social+network'

# Package the request, send the request and catch the response: r
r = requests.get(url)

# Print the text of the response
text = r.text
print(text)

print('------------- Other exercise from datacamp ----------------')
# Import package
import requests

# Assign URL to variable: url
url = 'http://www.omdbapi.com/?apikey=72bc447a&t=social+network'

# Package the request, send the request and catch the response: r
r = requests.get(url)

# Decode the JSON data into a dictionary: json_data
json_data = r.json()

# Print each key-value pair in json_data
for k in json_data.keys():
    print(k + ': ', json_data[k])

print("----------- Other exercise from DATACAMP ---------------")
# Import package
import requests

# Assign URL to variable: url
url = 'https://en.wikipedia.org/w/api.php?action=query&prop=extracts&format=json&exintro=&titles=pizza'

# Always include a descriptive User-Agent (Wikipedia requires this)
headers = {
    "User-Agent": "Checking out the Wikipedia API"
}

# Package the request, send the request and catch the response: r
r = requests.get(url, headers=headers)

# Decode the JSON data into a dictionary: json_data
json_data = r.json()

# Print the Wikipedia page extract
pizza_extract = json_data['query']['pages']['24768']['extract']
print(pizza_extract)
