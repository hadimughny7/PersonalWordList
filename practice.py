import requests

api_key = '29d4ca74-a7aa-4e3c-8922-a89a104c94eb'
word = 'potato'
url = f'https://www.dictionaryapi.com/api/v3/references/collegiate/json/{word}?key={api_key}'

res = requests.get(url)

definitions = res.json()

print(definitions)

for definition in definitions:
    print(definitions)