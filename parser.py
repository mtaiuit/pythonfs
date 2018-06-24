import requests
from bs4 import BeautifulSoup

req = requests.get('https://en.wikipedia.org/wiki/Python_(programming_language)')
soup = BeautifulSoup(req.text, "lxml")
for sub_heading in soup.find_all('h2'):
    print(sub_heading.text)