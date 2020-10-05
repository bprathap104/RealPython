import requests
url = 'https://httpbin.org/post'
response = requests.post(url, json={'key':'value'})
print(response)
print(response.request.url)
print(response.request.method)
print(response.request.body)

