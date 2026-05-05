from pathlib import Path
import logging
from dotenv import load_dotenv
import os

load_dotenv()

params = {"q": "программист", "page": "2"}

headers = {"User-Agent": os.getenv("USER_AGENT")}

HOME = Path.home() / "Desktop"
create_folder = HOME / "Logs-Parser"
create_folder.mkdir(exist_ok=True)
create_file = create_folder / "parser.txt"

logging.basicConfig(level=logging.DEBUG)

logger = logging.getLogger(__name__)
