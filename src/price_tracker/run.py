from price_tracker import UrlParser,

if __name__ == "__main__":
    url_parser = UrlParser("https://www.google.com", 45)
    print(url_parser.url, url_parser.title)

    library = LibraryPrice("https://www.google.com", 45)
    print(library)
    library.find_prices_library()
    print(ROOT_DIR)
    csv_lib = CsvURL(f"{ROOT_DIR}/{FILES}/test.csv")


