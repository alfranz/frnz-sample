import pandas as pd
from typing import Dict


def count_missing(dataframe: pd.DataFrame) -> Dict[str, int]:
    return dict(dataframe.isna().sum())
