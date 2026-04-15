# Importaciones
import pandas as pd
from src.data import DataProcessing

def main():
    
    data = DataProcessing()

    X, y = data.load_xy()


if __name__ == "__main__":
    main()