import requests

url = 'https://jsonplaceholder.typicode.com/posts/1'
response = requests.get(url)

print(response.json())


import requests

url = 'https://pokeapi.co/api/v2/pokemon-species/aegislash'
reepose = requests.get(url)

print(response.poke())



query = "https://pokeapi.co/v2/pokemon-species/mewtwo/"
response = requests.get(query)
print(response)
print(response.json())

 
if response == 200:
    data= response.json()

    filtered_data= {
         "name": data["name"],
         "height": data["height"],
         "weight": data["weight"],
         "types": data["types"],
         "abilities": [ability["ability"]["name"] for ability in data["abilites"]]
    }
    
    print(filtered_data)
else:
    print("data not found")

