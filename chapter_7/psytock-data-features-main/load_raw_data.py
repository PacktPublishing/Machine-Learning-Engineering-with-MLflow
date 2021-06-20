import mlflow
from datetime import date
from dateutil.relativedelta import relativedelta
import pprint
import pandas_datareader
import pandas

import pandas_datareader.data as web

if __name__ == "__main__":

    
    with mlflow.start_run(run_name="load_raw_data") as run:

        mlflow.set_tag("mlflow.runName", "load_raw_data")
        end = date.today()
        start = end + relativedelta(months=-3)
        
        df = web.DataReader("BTC-USD", 'yahoo', start, end)

        df.to_csv("./data/raw/data.csv")
