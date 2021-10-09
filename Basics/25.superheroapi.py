import requests
import json
data2 = requests.get("https://akabab.github.io/superhero-api/api/all.json")

superhero = json.loads(data2.text)

data = int(input("Please enter your power number: "))

for eachhero in superhero:
    if eachhero['powerstats']['intelligence'] == data and eachhero['powerstats']['strength'] == data and eachhero['powerstats']['power'] == data:
        print(eachhero['name'])