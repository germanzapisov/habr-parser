import requests
from bs4 import BeautifulSoup
from utils import *

session = requests.Session()


class HabrParser:
    @logger_decorator
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
        logger.debug('successful')
        return vacancies

    @logger_decorator
    def outputer(self):
        data = self.parse(soup)
        for vacancy in data['vacancy'].items():
            yield vacancy

    # @logger_decorator
    # def writer(self):
    #     pass


if __name__ == "__main__":
    time = time_now()

    response = session.get(url, **request_settings)

    soup = BeautifulSoup(response.text, "html.parser")

    Parser = HabrParser()
    Parser.parse(soup)

    output = Parser.outputer()
    for vacancy in output:
        print(vacancy)
