from bs4 import BeautifulSoup
from price_parser import Price
from ..BaseUrl import UrlParser


class ScrapePrice(UrlParser):

    def __init__(self, *args, **kwargs) -> None:
        super(self.__class__, self).__init__(*args, **kwargs)
        self.price = -1
        self.alert_flag = False

        self.find_prices_library()

    #Currently working only on scraping webpage
    def find_prices_library(self) -> None:

        html = self.response.text
        soup = BeautifulSoup(html, "lxml")

        el = soup.select_one('.price_color')
        try:
            self.price = Price.fromstring(el.text).amount_float
        except Exception as e:
            raise ValueError(e)

        self.alert_flag = self.price < self.alert_price

    def __str__(self):
        fstr = super(ScrapePrice, self).__str__() + f"is currently listed with the price of {self.price} and "
        if self.alert_flag:
            return fstr + "is on discount!"
        elif not self.alert_flag and self.price != "Not Available":
            return fstr + f"is not on discount!"
        else:
            return super(ScrapePrice, self).__str__() + f"is not available."



