import requests
import json

apiKey = 'somekey'
url = 'https://api.unsplash.com//users/olgarozhdestvina/likes/?client_id='
filename = 'static/unsplash_images.json'
response = requests.get(url+apiKey)

repoJSON = response.json()

file = open(filename, 'w')
json.dump(repoJSON, file, indent=4)