from src.price_tracker.CsvURL import CsvURL
from src.price_tracker.BaseUrl import UrlParser
from src.price_tracker.LibraryPrice import LibraryPrice
import os
import sys

FILES = "files"
ROOT_DIR = os.path.dirname(os.path.dirname(__file__)).split("\src")[0]

if len(sys.argv) < 3:
    raise TypeError(f"Not enough input arguments. (Expected 2, but got {len(sys.argv)})")
