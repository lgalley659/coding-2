import requests

url = 'https://jsonplaceholder.typicode.com/posts/1'
response = requests.get(url)

print(response.json())





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

