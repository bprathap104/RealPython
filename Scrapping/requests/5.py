# Query string parameters
import requests

response = requests.get('https://api.github.com/search/repositories',
            params={'q': 'cloud-custodian+language:python'},
            headers={'Accept':'application/vnd.github.v3.text-match+json'},
            )
# View the 'text-matches' array which provides information about your search term within the results
json_response = response.json()
for repo in json_response["items"]:
    print(f'Repository details: {repo["full_name"]}')  # Python 3.6+
    print(f'Text matches: {repo["text_matches"]}')
    print('')

