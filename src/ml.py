import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

class ModelML():

    def __init__(self, X:pd.DataFrame, y:pd.Series):
        self.X = X
        self.y = y

    def eval(self, model):

        # split
        X_train, X_test, y_train, y_test = train_test_split(self.X,self.y,test_size=0.2)

        # entrenamiento
        model.fit(X_train, y_train)

        # predicciones
        y_pred_train = model.predict(X_train)
        y_pred_test = model.predict(X_test)

        # metricas
        acc_train = accuracy_score(y_pred_train, y_train)
        acc_test = accuracy_score(y_pred_test, y_test)

        print(model)
        print(f"accuracy (train): {acc_train}")
        print(f"accuracy (test): {acc_test}")
