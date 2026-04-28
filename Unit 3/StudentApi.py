# use one of the following APIs to pull and access the data.

# Dog API -> return atleast 3 types of dogs
# https://dog.ceo/dog-api/

# Cat API -> return atleast 3 types of cats
# https://http.cat/

# Rick and Morty API -> return at least 3 rick and morty characters
# https://rickandmortyapi.com/


import requests

url = 'https://dog.ceo/api/breeds/image/random'
response = requests.get(url)

print(response.json())

if 
    print(filtered_data)
else:
    print("data not found")
