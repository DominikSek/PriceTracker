from price_tracker import UrlParser, LibraryPrice, CsvURL


def run(file_path, variation):
    url_parser = UrlParser("https://www.google.com", 45)
    print(url_parser.url, url_parser.title)

    library = LibraryPrice("https://www.google.com", 45)
    print(library)
    library.find_prices_library()

    csv_lib = CsvURL(file_path, variation)

