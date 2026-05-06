
def menu():
    choice_query = input("""
    Введите запрос
    >>>""")
    choice_page = int(input("""Выберите страницу для парсинга
    >>>"""))
    return choice_query, choice_page

