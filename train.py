# Importaciones
import pandas as pd
from src.data import DataProcessing
from src.ml import ModelML
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier

def main():
    
    data = DataProcessing()

    # matriz de caracteristicas y target
    X, y = data.load_xy()

    # evaluacion de modelo de machine learning
    #model = LogisticRegression(max_iter=10000)
    model = DecisionTreeClassifier(max_depth=7)
    ml = ModelML(X,y)
    ml.eval(model=model)


if __name__ == "__main__":
    main()