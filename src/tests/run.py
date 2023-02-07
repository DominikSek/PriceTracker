from src.price_tracker.base import UrlParser
from src.price_tracker.library_price import LibraryPrice

if __name__ == "__main__":
    url_parser = UrlParser("https://www.google.com")
    print(url_parser.url, url_parser.title)

    library = LibraryPrice("https://www.google.com")
    print(library)
    library.find_prices_library()


