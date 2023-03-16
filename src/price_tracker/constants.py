# File for constants
from pathlib import Path

_ABS_PATH = str(Path(__file__).resolve().parents[2])
LIBRARY = 0
RAW = 1
FILES_PATH = _ABS_PATH + "/files"
URL_FILE = "url_data.csv"
SAVE_PATH = _ABS_PATH + "/save"
SAVE_TO_CSV = True
PRICES_CSV = "prices.csv"
SEND_MAIL = True
HEADER = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36",
    'Accept': '*/*', 'Accept-Encoding': 'gzip, deflate, br', 'Accept-Language': 'en-GB,en-US;q=0.9,en;q=0.8'
}
