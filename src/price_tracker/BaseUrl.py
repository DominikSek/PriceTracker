# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import requests
import validators
from bs4 import BeautifulSoup
from urllib.parse import urlparse
from .constants import HEADER


class UrlParser:

    def __init__(self, url, alert_price) -> None:
        self.url = url
        self.response = None
        self.get_response(url)

        self.title = self.get_title().strip()
        self.alert_price = alert_price
        self.domain = urlparse(url).netloc

    def get_response(self, url) -> None:
        validate = validators.url(url)

        #if not validate:
        #    raise Exception(f"Url: '{url}' is not valid.")
        try:
            self.response = requests.get(url, headers=HEADER)
        except requests.exceptions.RequestException as e:
            raise SystemExit(e)

    def get_title(self) -> str:
        soup = BeautifulSoup(self.response.text, 'html.parser')
        return soup.find_all('title')[0].get_text()

    def __str__(self) -> str:
        print_title = (self.title[:45] + '...') if len(self.title) > 75 else self.title
        return f"{print_title}\twith the alert price: {self.alert_price} €\n"
