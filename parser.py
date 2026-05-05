import requests
from bs4 import BeautifulSoup
from utils import *
from datetime import datetime as dt

url = 'https://career.habr.com/vacancies'

session = requests.Session()

def parser(finder):
    with open (create_file, 'a') as file:
        for f in finder:
            for vacancy in f.select('.vacancy-card__title-link'):
                file.write(f"\n{dt.now().strftime('%M.%d %H:%M.%S')}\nvacancy: {vacancy.get_text()}")
            for price in f.select('.basic-salary'):
                file.write(f'\n{price.get_text()}')
            for price_none in f.select('.predicted-salary__title--margin-s'):
                file.write(f'\n{price_none.get_text()}')
            file.write('\n____________________')
        file.write('\nsuccessful ' + dt.now().strftime('%M.%d %H:%M.%S'))


if __name__ == '__main__':
    response = session.get(url, params=params)

    soup = BeautifulSoup(response.text, 'html.parser')

    finder = soup.find_all("div", class_='vacancy-card__info')
    parser(finder)

