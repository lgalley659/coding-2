import requests

url = 'https://jsonplaceholder.typicode.com/posts/1'
response = requests.get(url)

print(response.json())


import requests

url = 'https://bored-api.appbrewery.com/random'

print(response.bored())