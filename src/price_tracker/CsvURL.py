import pandas as pd

from price_tracker import LibraryPrice, RawPrice

LIBRARY = 0
RAW = 1


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

    def fetch_urls(self, dataframe) -> dict:
        pass





