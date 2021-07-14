import mlflow
from datetime import date
from dateutil.relativedelta import relativedelta
import pprint
import pandas_datareader
import pandas
import requests

import pandas_datareader.data as web

if __name__ == "__main__":

    #Workaround to handle issue https://github.com/pydata/pandas-datareader/issues/868
    USER_AGENT = {
        'User-Agent': ('Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)'
                    ' Chrome/91.0.4472.124 Safari/537.36')
        }
    sesh = requests.Session()
    sesh.headers.update(USER_AGENT)

    
    with mlflow.start_run(run_name="load_raw_data") as run:

        mlflow.set_tag("mlflow.runName", "load_raw_data")
        end = date.today()
        start = end + relativedelta(months=-3)
	
        
        df = web.DataReader("BTC-USD", 'yahoo', start, end, session=sesh)

        df.to_csv("./data/raw/data.csv")
