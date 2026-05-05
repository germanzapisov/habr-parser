import requests
from bs4 import BeautifulSoup

url = 'https://career.habr.com/vacancies'

session = requests.Session()

params = {
    'q': 'программист',
    'page': '2'
}

response = session.get(url, params=params)

soup = BeautifulSoup(response.text, 'html.parser')

finder = soup.find_all("div",class_='vacancy-card__info')


for f in finder:
    for vacancy in f.select('.vacancy-card__title-link'):
        print('vacancy: '+ vacancy.get_text())
    for price in f.select('.basic-salary'):
        print(price.get_text())
    for price_none in f.select('.predicted-salary__title--margin-s'):
        print(price_none.get_text())
    print('____________________')

