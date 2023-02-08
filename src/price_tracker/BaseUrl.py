# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import requests
import validators
from bs4 import BeautifulSoup


class UrlParser:

    def __init__(self, url, alert_price) -> None:
        self.response = self.get_response(url)

        self.url = url
        self.title = self.get_title()
        self.alert_price = alert_price

    @staticmethod
    def get_response(url) -> requests.Response:
        validate = validators.url(url)

        if not validate:
            raise Exception(f"Url: '{url}' is not valid.")
        try:
            r = requests.get(url)
            return r
        except requests.exceptions.RequestException as e:
            raise SystemExit(e)

    def get_title(self) -> str:
        reqs = requests.get(self.url)
        soup = BeautifulSoup(reqs.text, 'html.parser')

        return soup.find_all('title')[0].get_text()

    def __str__(self) -> str:
        return f"{self.title} with the price: {self.alert_price} €\n{self.url}"
