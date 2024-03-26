import pandas as pd
import os

def get_training():
    X = pd.read_csv("./data/X_train.csv", index_col=False)
    y = pd.read_csv("./data/y_train.csv", index_col=False)
    X = X.select_dtypes(exclude=['object'])
    return X, y