import requests
from bs4 import BeautifulSoup
from utils import *



session = requests.Session()


class HabrParser:
    def parse(self, soup) -> dict:
        finder = soup.find_all("div", class_="vacancy-card__info")
        vacancies = {"vacancy": {}}
        for f in finder:
            vacancy = f.select_one(".vacancy-card__title-link")
            price = f.select_one(".basic-salary")
            if price:
                vacancies["vacancy"][vacancy.get_text()] = [price.get_text()]
            elif not price:
                salary = f.select_one(".predicted-salary__title--margin-s")
                if salary:
                    vacancies["vacancy"][vacancy.get_text()] = [
                        salary.get_text()
                    ]
                if not salary:
                    salary = "----------"
                    vacancies["vacancy"][vacancy.get_text()] = [salary]
        return vacancies

    def outputer(self):
        data = Parser.parse(soup)
        for vacancy in data['vacancy'].items():
            yield vacancy

    def writer(self):
        pass


if __name__ == "__main__":
    time = time_now()

    response = session.get(url, **request_settings)

    soup = BeautifulSoup(response.text, "html.parser")

    Parser = HabrParser()
    Parser.parse(soup)


    for i in Parser.outputer():
        print(i)
    print(f"{time} | successful")

