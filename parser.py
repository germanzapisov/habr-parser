import requests
from bs4 import BeautifulSoup
from utils import *
from datetime import datetime as dt

url = 'https://career.habr.com/vacancies'

session = requests.Session()

# def parser(finder, vacancies):
#     with open (create_file, 'a') as file:
#         logger.debug('Начало работы..')
#         for f in finder:
#             for vacancy in f.select('.vacancy-card__title-link'):
#                 vacancies['vacancy'][vacancy.get_text()] = []
#             for price in f.select('.basic-salary'):
#                 vacancies['vacancy'][vacancy.get_text()].append(price)
#             for price_none in f.select('.predicted-salary__title--margin-s'):
#                 vacancies['vacancy'][vacancy.get_text()].append(price)
#         file.write('\nsuccessful ' + dt.now().strftime('%M.%d %H:%M.%S'))
#         logger.debug('Информация успешно выдана!')

def new_parser(finder, vacancies):
    for f in finder:
        vacancy = f.select_one(".vacancy-card__title-link")
        price = f.select_one(".basic-salary")
        if price:
            vacancies['vacancy'][vacancy.get_text()] = [price.get_text()]
        elif not price:
            salary = f.select_one('.predicted-salary__title--margin-s')
            vacancies['vacancy'][vacancy.get_text()] = [salary]
            if not salary:
                salary = 'ЗП не указана'
                vacancies['vacancy'][vacancy.get_text()] = [salary]


    for vacancy, price in vacancies['vacancy'].items():
        print(vacancy, price, '\n')

def writer():
    pass

if __name__ == '__main__':
    response = session.get(url, params=params)
    vacancies = {'vacancy':{}}
    soup = BeautifulSoup(response.text, 'html.parser')

    finder = soup.find_all("div", class_='vacancy-card__info')
    new_parser(finder, vacancies)
