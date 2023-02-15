import pandas as pd
from .Variations.ScrapePrice import ScrapePrice
from .Variations.RawPrice import RawPrice
from . import constants
import warnings
import math


class CsvURL:

    def __init__(self, filename, type, percentage) -> None:
        self.urls = {}
        self.type = type
        try:
            dataframe = pd.read_csv(filename)
        except FileNotFoundError:
            raise FileNotFoundError(f"File {filename} does not exist.")
        except Exception as e:
            raise SystemExit(e)

        self.fetch_urls(dataframe, percentage)

    def fetch_urls(self, dataframe, percentage) -> None:
        for row in dataframe.to_dict("records"):
            if not row["alert_price"]:
                warnings.warn(f"Alert price for the url {row['urls']} is missing.")
            elif math.isnan(row["alert_price"]):
                warnings.warn(f"Alert price for the url {row['urls']} is not a number")
            if self.type == constants.LIBRARY:
                self.urls[row["ID"]] = ScrapePrice(row["urls"], row["alert_price"], percentage)
            else:
                self.urls[row["ID"]] = RawPrice(row["urls"], row["alert_price"], percentage)

    def __str__(self) -> str:
        fstr = ""
        for id, url in self.urls.items():
            fstr += f"ID = {id}\n"
            fstr += f"{url}\n"
            fstr += f"------------------------------------\n"
        return fstr






