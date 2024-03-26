import pandas as pd
import os

def get_training():
    X = pd.read_csv("../data/X_train.csv", usecols=lambda column: column != 'id')
    y = pd.read_csv("../data/y_train.csv", usecols=lambda column: column != 'id')
    X = X.select_dtypes(exclude=['object'])
    return X, y