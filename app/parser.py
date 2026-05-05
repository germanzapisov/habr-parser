import requests
from bs4 import BeautifulSoup
from utils import *
from datetime import datetime as dt

url = "https://career.habr.com/vacancies"

session = requests.Session()


class HabrParser:
    def new_parser(self):
        finder = soup.find_all("div", class_="vacancy-card__info")
        vacancies = {"vacancy": {}}
        for f in finder:
            self.vacancy = f.select_one(".vacancy-card__title-link")
            self.price = f.select_one(".basic-salary")
            if self.price:
                vacancies["vacancy"][self.vacancy.get_text()] = [self.price.get_text()]
            elif not self.price:
                self.salary = f.select_one(".predicted-salary__title--margin-s")
                if self.salary:
                    vacancies["vacancy"][self.vacancy.get_text()] = [
                        self.salary.get_text()
                    ]
                if not self.salary:
                    self.salary = "----------"
                    vacancies["vacancy"][self.vacancy.get_text()] = [self.salary]
        for vacancy, price in vacancies["vacancy"].items():
            print(vacancy, price, "\n")

    def writer(self):
        pass


if __name__ == "__main__":
    response = session.get(url, params=params, headers=headers)

    soup = BeautifulSoup(response.text, "html.parser")

    Parser = HabrParser()
    Parser.new_parser()
