import pandas as pd
from src.config import DATA_PATH, FEATURES, TARGET

class DataProcessing():
    '''
    Objetivo: Se encarga de la ingesta y preprocesamiento de datos
    '''
    def __init__(self, n_samples: int = None):
        self.n_samples = n_samples

    def load_data(self):
        df = pd.read_csv(DATA_PATH, usecols=FEATURES+[TARGET])
        
        if self.n_samples is not None and type(self.n_samples) != int:
            raise ValueError("n_samples debe ser un valor entero o nulo")

        if self.n_samples:
            df = df.sample(n=self.n_samples, random_state=42)


        return df
    
    def load_xy(self):
        df = self.load_data()

        X = df[FEATURES]
        y = df[TARGET]

        return X, y