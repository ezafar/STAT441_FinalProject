import pandas as pd
import os

def get_training(exlude_obj=False):
    X = pd.read_csv("../data/X_train.csv", index_col=0)
    y = pd.read_csv("../data/y_train.csv", index_col=0)
    y[y == -1] = 0
    if exlude_obj:
        X = X.select_dtypes(exclude=['object'])
    return X, y

def get_test():
    X_test = pd.read_csv('../data/X_test.csv', index_col=0)
    return X_test

def get_predictions(X_test, model, proba=True, name=None):
    if proba:
        y_pred = model.predict_proba(X_test)
    else:
        y_pred = model.predict(X_test)
    preds_df = pd.DataFrame(y_pred, columns=['no answer', 'very important', 'quite important', 'not important', 'not at all important'])
    preds_df.index.name = 'id'
    if name is not None:
        preds_df.to_csv(f"../data/predictions/{name}.csv")
    return preds_df
    

def drop_objects(X):
    return X.select_dtypes(exclude=['object'])
