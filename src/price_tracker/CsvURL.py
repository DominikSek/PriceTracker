import pandas as pd


class CsvURL:

    def __init__(self, filename):
        self.urls = pd.read_csv(filename)
        print(self.urls)