import requests
from bs4 import BeautifulSoup

URL = 'https://www.amazon.in/s?k=python+the+hard+way&i=digital-text&ref=nb_sb_noss_2'
custom_cookie = {'cookie_name': 'cookie_value'}

session = requests.Session()
# print(session.cookies.get_dict())
page = requests.get(URL,cookies=custom_cookie)
soup = BeautifulSoup(page.content, features="html5lib")
# divs = soup.findAll({'class': 'rush-component'})
divs = soup.findAll(class_='rush-component')
for d in divs:
    print(d.find())

# print(page.text)


# session = requests.Session()
# print(session.cookies.get_dict())

# response = session.get('http://google.com')
# print(session.cookies)


