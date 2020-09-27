import pandas as pd


def count_missing(dataframe: pd.DataFrame):
    return dict(dataframe.isna().sum())