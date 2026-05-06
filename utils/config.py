from pathlib import Path
import logging
from dotenv import load_dotenv
import os
from app.menu import menu

load_dotenv()

choice_query, choice_page = menu()

print(choice_query)
params = {"q": choice_query, "page": choice_page}

url = "https://career.habr.com/vacancies"

headers = {"User-Agent": os.getenv("USER_AGENT")}

HOME = Path.home() / "Desktop"
create_folder = HOME / "Logs-Parser"
create_folder.mkdir(exist_ok=True)
create_file = create_folder / "parser.txt"

logging.basicConfig(level=logging.DEBUG)

logger = logging.getLogger(__name__)
