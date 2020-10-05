# Query string parameters
import requests

response = requests.get('https://api.github.com/search/repositories',
            params={'q': 'cloud-custodian+language:python'},
            )
# Inspect some attributes of the repository
json_response = response.json()
for repo in json_response["items"]:
    print(f'Repository details: {repo["full_name"]}')  # Python 3.6+
    print(f'Repository description: {repo["description"]}')
    print('')
