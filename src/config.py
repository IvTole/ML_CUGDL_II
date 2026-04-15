# Variables de configuracion

# Data path
DATA_PATH = "https://raw.githubusercontent.com/IvTole/MachineLearning_InferenciaBayesiana_CUGDL/refs/heads/main/data/titanic/titanic_clean.csv"

# Features and target

FEATURES = ['pclass', 'sex', 'age',
       'embarked_Q', 'embarked_S', 'isalone',
       'title_Miss', 'title_Mr', 'title_Mrs', 'title_Rare', 'fare_log',
       'familysize_log']

TARGET = "survived"