import pandas as pd
import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from price_tracker import run

if __name__ == "__main__":
    run("raw")

