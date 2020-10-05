import requests

def print_d(json):
    [print(f'{key}: {value}') for key, value in json.items()]


url = 'https://api.github.com/'

response = requests.get(url)

print(response.content)   # Byte format

print(response.text)      # Text String

json1 = response.json()   # JSON format output

print_d(json1)

print(json1['repository_url'])

headers = response.headers  # Headers

print(headers)

print(response.headers['content-type'])  # case-insenstitve







