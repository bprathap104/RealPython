import requests
from getpass import getpass
from requests.auth import HTTPBasicAuth

# url='https://api.github.com/user'
# #response=requests.get(url, auth=('bprathap104', getpass()))    # Deprecated this call in Github
# #print(response.content)
# response=requests.get(url, auth=HTTPBasicAuth('bprathap104', getpass()))
# print(response.status_code)

blog_url='https://webapptech.herokuapp.com/post?id=1'
response = requests.get(blog_url)
print(response.status_code)
# print(response.json())
print(response.headers)
