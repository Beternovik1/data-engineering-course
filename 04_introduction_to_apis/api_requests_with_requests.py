# Import the requests package
import requests

# Pass the API URL to the get function
response = requests.get('http://localhost:3000/lyrics')

# Print out the text attribute of the response object
print(response.text)

# --------------------------------------------------
print("---------- Exercises from datacamp --------------")
# Get a list of all playlists from the API
response = requests.get('http://localhost:3000/playlists')
print(response.text)

# Create a dictionary with the playlist info
playlist_data = {'Name': 'Rock Ballads'}

# Perform a POST request to the playlists API with your dictionary as data parameter
response = requests.post('http://localhost:3000/playlists', data=playlist_data)
print(response.text)

# Perform a GET request to get info on playlist with PlaylistId 2
response = requests.get('http://localhost:3000/playlists/2')

print(response.text)

# Perform a DELETE request to the playlist API using the path to playlist with PlaylistId 2
requests.delete('http://localhost:3000/playlists/2')

# Get the list of all existing playlists again
response = requests.get('http://localhost:3000/playlists')
print(response.text)