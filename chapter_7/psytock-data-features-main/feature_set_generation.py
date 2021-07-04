import mlflow
from datetime import date
from dateutil.relativedelta import relativedelta
import pprint
import pandas as pd
import pandas_datareader
import pandas_datareader.data as web
import numpy as np

def rolling_window(a, window):
    """
        Takes np.array 'a' and size 'window' as parameters
        Outputs an np.array with all the ordered sequences of values of 'a' of size 'window'
        e.g. Input: ( np.array([1, 2, 3, 4, 5, 6]), 4 )
             Output: 
                     array([[1, 2, 3, 4],
                           [2, 3, 4, 5],
                           [3, 4, 5, 6]])
    """
    shape = a.shape[:-1] + (a.shape[-1] - window + 1, window)
    strides = a.strides + (a.strides[-1],)
    return np.lib.stride_tricks.as_strided(a, shape=shape, strides=strides)


if __name__ == "__main__":
    with mlflow.start_run() as run:

        mlflow.set_tag("mlflow.runName", "feature_set_generation")

        raise Exception('x should not exceed 5. The value of x was: {}'.format(x))

        btc_df = pd.read_csv("data/staging/data.csv")

        btc_df['delta_pct'] = (btc_df['Close'] - btc_df['Open'])/btc_df['Open']

        btc_df['going_up'] = btc_df['delta_pct'].apply(lambda d: 1 if d>0.00001 else 0).to_numpy()

        element=btc_df['going_up'].to_numpy()

        WINDOW_SIZE=15

        training_data = rolling_window(element, WINDOW_SIZE)

        pd.DataFrame(training_data).to_csv("data/training/data.csv")