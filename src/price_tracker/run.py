from . import CsvURL, constants
## Napravi logger https://stackoverflow.com/questions/384076/how-can-i-color-python-logging-output
## Dodati da custom postotak koristis za popust


def run(variation, percentage=0.2) -> None:

    if percentage < 0 or percentage > 1:
        raise SyntaxError(f"Percentage cannot be less than 0.00, or greater than 1.00.")

    if variation.upper() == "LIBRARY":
        csv_lib = CsvURL(constants.FILE_PATH, constants.LIBRARY, percentage)
    elif variation.upper() == "RAW":
        csv_lib = CsvURL(constants.FILE_PATH, constants.RAW, percentage)
    else:
        raise SyntaxError(f"Wrong variation ({variation}), only library and raw exist.")

    print(csv_lib)

