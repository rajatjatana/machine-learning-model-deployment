import pandas as pd
from sklearn.base import BaseEstimator , TransformerMixin


class CategoricalImputer(BaseEstimator , TransformerMixin) :
    """ Categorical data missing value imputer"""

    def __init__(selfself , variables=None):
