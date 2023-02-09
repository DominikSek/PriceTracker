from . import UrlParser, CsvURL, constants
from .Variations import LibraryPrice, RawPrice


def run(variation) -> None:

    if variation.upper() == "LIBRARY":
        csv_lib = CsvURL(constants.FILE_PATH, constants.LIBRARY)
    elif variation.upper() == "RAW":
        csv_lib = CsvURL(constants.FILE_PATH, constants.RAW)
    else:
        raise SyntaxError(f"Wrong variation ({variation}), only library and raw exist.")

    print(csv_lib)

