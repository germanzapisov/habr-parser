from pathlib import Path
import logging
from dotenv import load_dotenv
import os
from app.menu import menu
from datetime import datetime as dt

load_dotenv()


def time_now() -> str:
    time = dt.now().strftime('%m.%d %H:%M %S')
    return time


choice_query, choice_page = menu()

request_settings = {
    'params': {"q": choice_query, "page": choice_page},
    'headers': {"User-Agent": os.getenv("USER_AGENT")}
}

url = "https://career.habr.com/vacancies"


HOME = Path.home() / "Desktop"
create_folder = HOME / "Logs-Parser"
create_folder.mkdir(exist_ok=True)
create_file = create_folder / "parser.txt"

logging.basicConfig(level=logging.DEBUG)

logger = logging.getLogger(__name__)
