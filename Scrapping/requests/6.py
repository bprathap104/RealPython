import requests
url = 'http://httpbin.org/'
response = requests.post(url + 'post', data={'key':'value'})
print(response)
print(response.content)     # This method calling not allowed in post
print(response.status_code)
print(response.headers)
print(response.headers['content-type'])

payload={'key':'value'}
response = requests.put(url + 'put', data=payload)
print(response)
print(response.status_code)
print(response.content)
print(response.json())
print(response.headers)
print(response.headers['content-type'])

response = requests.delete(url + 'delete')
print(response)
print(response.status_code)
print(response.content)
print(response.json())
print(response.headers)
print(response.headers['content-type'])
