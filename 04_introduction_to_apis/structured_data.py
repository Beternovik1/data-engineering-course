# Complex data structures
#   - Lyric API response
#     The lyric API returns the lyric as unstructured text
#       * response line
#           HTTP/1.1 200 OK 
#       * headers
#           Content-Type: plain/text
#           Content-Language: en-US
#           Last-Modified: Weed, 21 Oct 2023 07:28:00 GMT
#       * body
#           N' I never miss Cause I'm a problem
#           child -AC/DC, problem Child

#   - Album API response
#     The Album API requeres more structure to transmit effectively
#     because albums have multiple properties
#       * response line:
#           HTTP/1.1 200 OK
#       * headers
#           Content-Type: application/json
#           Content-Language: en_US
#           Last-Modified: Wed, 21 Oct 2023 07:28:00 GMT
#       * body
#           {
#               "id": 42,
#               "title": "Back in Black",
#               "artist": "AC/DC",
#               "tracks": [
#                   { "id": 1, "title": "Hells bells" },
#                   { "id": 2, "title": "Shoot to Thrill" },
#                   { "id": 3, "title": "What Do You ..." },
#                   { "id": 4, "title": "Givin the Dog ..." },
#                   { "id": 5, "title": "Let Me Put my ..." }
#               ]
#            }

# Complex data structures: JSON
#   - JSON
#       * JavaScript Object Notation
#       * Widely supported
#       * Human readable and machine usable
#   - Content-type, mime-type or media-type
#   - Other formats
#       * XML
#       * CSV
#       * YAML

# ------------------------------------------------------------------------
# Note: Python Object are only the simple built-in structures 
# (dict, list, str, int, bool, None).

# From Python to JSON and back
#   - In order to use a python object with web API, we first need
#     to converti it to a JSON string so we can safely transmit it with the
#     the request or response

#   - Transforming a python object to JSON is called "ENCODING"
#   - Transforming a JSON string back into a python object is called "DECODING"

# In python the built-in 'json' package can encode and decode JSON
import json
album = {'id':42, 'title': "Back in Black"}
string = json.dumps(album) # Encodes a python object to a JSON string
album = json.loads(string) # Decodes a JSON string to a Python object 

# ----------------------------------------------------------------------
# Requesting JSON data - Receiving JSON data

# GET request without headers
# Without adding additional headers, the server will respond in plain text
import requests
response = requests.get('http://api.music-catalog.com/lyrics')
print(response.text)
# Output
# N' I never miss Cause I'm a problem child - AC/DC, Problem Child

# GET request with an accept header
# When we add an accept header with the value 'application/json', the server 
# will respond with JSON text
response = requests.get('http://api.music-catalog.com/lyrics', headers={'accept':'application/json'})
# Print the JSON text 
print(response.text)
# Output
# {'artist':'AC/DC', 'lyric': "N' I never miss Cause I'm a problem child - AC/DC, Problem Child", 
# 'track': 'Probelm Child'}
# Decode into a Python object and printing the artist attribute 
data = response.json()
print(data['artist'])

# Sending JSON data
import requests
playlist = {"name": "Road trip", "genre":"rock", "private":"true"}
# Add the plyalist using via the 'json' argument
# requests will automatically add the necessary content-type headers
# and do all of the encoding 
response = requests.post("http://api.music-catalog.com/playlists", json=playlist)

# Get the request object
request = response.request

# Print the request content-type header
print(request.headers['content-type'])
# Output
# application/json

# -------------------- DATACAMP EXERCISES -------------------------------
# 1. Receiving JSON with the requests package
#   - Add the correct header to request JSON from the API.
#   - Decode the JSON response into an album object.
#   - Print the album Title property

headers = {
    'Authorization': 'Bearer ' + API_TOKEN,
    # Add a header to request JSON formatted data
    'accept': 'application/json'
}
response = requests.get('http://localhost:3000/albums/1/', headers=headers)

# Get the JSON data as a Python object from the response object
album = response.json()

# Print the album title
print(album['Title'])

# 2. Sending JSON with the requests package
#   - Pass the playlists variable as an argument to the requests.post() 
#       method so that it will be automatically sent as JSON.
#   - Get a list of all playlists from the API.
#   - Inspect the response of the GET request by printing the JSON text.
playlists = [{"Name":"Rock ballads"}, {"Name":"My favorite songs"}, {"Name":"Road Trip"}]

# POST the playlists array to the API using the json argument
requests.post('http://localhost:3000/playlists/', json=playlists)

# Get the list of all created playlists
response = requests.get('http://localhost:3000/playlists')

# Print the response text to inspect the JSON text
print(response.text)