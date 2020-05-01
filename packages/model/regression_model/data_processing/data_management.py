import pandas as pd
import os

from sklearn.externals import joblib
from sklearn.pipeline import Pipeline
from regression_model.config import config


def load_dataset(* , file_name: str) -> pd.DataFrame:
    # read the data from the path specified in config file:
    _data = pd.read_csv(f'{config.DATASET_DIR}/{file_name}')
    return _data
