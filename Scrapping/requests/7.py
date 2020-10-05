import requests
url = 'https://httpbin.org/post'

json_payload = {'key':'value'}

response = requests.post(url, data=json_payload)

print(response)
print(response.content)
print(response.status_code)
print(response.json()['headers']['Content-Type'])   # Returns application/x-www-form-urlencoded

tuple_payload = [('key','value'),('key1','value1')]
response = requests.post(url, data=tuple_payload)
print(response)
print(response.content)
print(response.status_code)
print(response.json()['headers']['Content-Type'])   # Returns application/x-www-form-urlencoded

json_payload = {'key':'value'}

response = requests.post(url, json=json_payload)
print(response)
print(response.content)
print(response.status_code)
print(response.json()['headers']['Content-Type'])   # Returns application/json




