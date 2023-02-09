import requests
from bs4 import BeautifulSoup
from lxml import etree as et
import time
import random
import csv
from ..BaseUrl import UrlParser


class RawPrice(UrlParser):

    def __init__(self, *args, **kwargs) -> None:
        super(self.__class__, self).__init__(*args, **kwargs)
        self.price = -1
        self.alert_flag = False
        self.find_raw_prices_library()

    #Currently working only on scraping webpage
    def find_raw_prices_library(self) -> None:
        soup = BeautifulSoup(self.response.content, "html.parser")
        dom = et.HTML(str(soup))

        try:
            price = dom.xpath('//span[@class="a-offscreen"]/text()')[0]
            self.price = price.replace(',', '').replace('€', '').replace('.00','')
        except Exception as e:
            self.price = "Not Available"

    def __str__(self) -> str:
        fstr = super(RawPrice, self).__str__() + f"is currently listed with the price of {self.price} and "
        if self.alert_flag:
            return fstr + "is on discount!"
        elif not self.alert_flag and self.price != "Not Available":
            return fstr + f"is not on discount!"
        else:
            return super(RawPrice, self).__str__() + f"is not available."



