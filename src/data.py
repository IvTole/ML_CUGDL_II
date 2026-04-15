import pandas as pd
from src.config import DATA_PATH, FEATURES, TARGET

class DataProcessing():

    def __init__(self, n_samples=None):
        self.n_samples = n_samples

    def load_data(self):
        df = pd.read_csv(DATA_PATH, usecols=FEATURES+[TARGET])

        return df
    
    def load_xy(self):
        df = self.load_data()

        X = df[FEATURES]
        y = df[TARGET]

        return X, y