from src.price_tracker.base import UrlParser


class LibraryPrice(UrlParser):

    def find_prices_library(self) -> dict:
        print(f"Getting the prices using a pre made library")

        print("Done")
        return dict()