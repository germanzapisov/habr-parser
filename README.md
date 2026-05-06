# 🧑‍💻 Habr Parser

Парсер вакансий с сайта **Habr Career**.
Собирает названия вакансий и информацию о зарплате.

---

## 🚀 Возможности

* 📄 Парсинг вакансий с https://career.habr.com/vacancies
* 💰 Получение зарплаты (если указана)
* ⚠️ Обработка случаев без зарплаты
* 🔁 Генератор для итерации по результатам

---

## 🛠️ Стек

* Python 3.10+
* requests
* beautifulsoup4

---

## 📦 Установка

```bash
git clone https://github.com/your-username/habr-parser.git
cd habr-parser

python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate

pip install -r requirements.txt
```

---

## ⚙️ Настройки

Создай файл `.env`:

```env
BASE_URL=https://career.habr.com/vacancies
USER_AGENT=Mozilla/5.0 (Windows AT 10 win64;x64)
```

---

## ▶️ Запуск

```bash
python main.py
```

---

## 📌 Пример вывода

```text
Python Developer — 150 000 ₽
Backend Engineer — ----------
Data Scientist — 200 000 ₽
```

---

## 🧱 Структура проекта

```text
project/
├── app/
│   ├──  parser.py
│   └──  menu.py
├── utils/
│   ├── __init__.py
│   └── config.py
├── requirements.txt
├── dev-requirements.txt
├── .env
└── README.md
```
