import requests

def print_d(json):
    [print(f'{key}: {value}') for key, value in json.items()]


url = 'https://api.github.com/'

response = requests.get(url)

print(response.content)   # Byte format

print(response.text)      # Text String

json1 = response.json()

print_d(json1)




