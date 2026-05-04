import requests
from bs4 import BeautifulSoup

url = 'https://career.habr.com/vacancies'

session = requests.Session()

params = {
    'query': 'программист'
}

response = session.get(url, params=params)

soup = BeautifulSoup(response.text, 'html.parser')

finder = soup.find_all("div",class_='vacancy-card__info')


for f in finder:
    for c in f.select('.vacancy-card__title-link'):
        print(c.get_text())
