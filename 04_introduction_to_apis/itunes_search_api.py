import requests
import json

url = "https://itunes.apple.com/search"

query_params = {'term': 'Zoe', 'media': 'music', 'limit': 1}

response = requests.get(url, params=query_params)

print(response.text)