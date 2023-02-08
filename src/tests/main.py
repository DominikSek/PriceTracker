from price_tracker import run
import pandas as pd

if __name__ == "__main__":
    run("../../files/test.csv", 1)
    a = pd.read_csv("../../files/test.csv")
