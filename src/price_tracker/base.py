# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import requests
import validators
from bs4 import BeautifulSoup
from requests import Response


class UrlParser:

    def __init__(self, url):
        self.response = self.get_response(url)

        self.url = url
        self.title = self.get_title()

    @staticmethod
    def get_response(url) -> Response:
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

    def __str__(self):
        return f"{self.title}\n{self.url}"