import pandas as pd
from .Variations.LibraryPrice import LibraryPrice
from .Variations.RawPrice import RawPrice
from . import constants


class CsvURL:

    def __init__(self, filename, type) -> None:
        self.urls = {}
        self.type = type
        try:
            dataframe = pd.read_csv(filename)
        except FileNotFoundError:
            raise FileNotFoundError(f"File {filename} does not exist.")
        except Exception as e:
            raise SystemExit(e)

        self.fetch_urls(dataframe)

    def fetch_urls(self, dataframe) -> None:
        for row in dataframe.to_dict("records"):
            if self.type == constants.LIBRARY:
                self.urls[row["ID"]] = LibraryPrice(row["urls"], row["alert_price"])
            else:
                self.urls[row["ID"]] = RawPrice(row["urls"], row["alert_price"])

    def __str__(self):
        fstr = ""
        for id, url in self.urls.items():
            fstr += f"{id}{url}\n"
        return fstr






