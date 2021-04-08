import mlflow
from datetime import date
from dateutil.relativedelta import relativedelta
import pprint
import pandas_datareader
import pandas
from pandas_profiling import ProfileReport
import great_expectations as ge
from great_expectations.profile.basic_dataset_profiler import BasicDatasetProfiler


if __name__ == "__main__":
    with mlflow.start_run(run_name="check_verify_data") as run:

        mlflow.set_tag("mlflow.runName", "check_verify_data")

        df = pandas.read_csv("./data/raw/data.csv")

        describe_to_dict=df.describe().to_dict()
        mlflow.log_dict(describe_to_dict,"describe_data.json")

        pd_df_ge = ge.from_pandas(df)

        assert pd_df_ge.expect_column_values_to_match_strftime_format("Date", "%Y-%m-%d").success == True
        assert pd_df_ge.expect_column_values_to_be_of_type("High", "float").success == True
        assert pd_df_ge.expect_column_values_to_be_of_type("Low", "float").success == True
        assert pd_df_ge.expect_column_values_to_be_of_type("Open", "float").success == True
        assert pd_df_ge.expect_column_values_to_be_of_type("Close", "float").success == True
        assert pd_df_ge.expect_column_values_to_be_of_type("Volume", "long").success == True
        assert pd_df_ge.expect_column_values_to_be_of_type("Adj Close", "float").success == True

        #we can do some basic cleaning by dropping the null values
        df.dropna(inplace=True)

        #if data_passes_quality_can_go_to_features:
        df.to_csv("data/staging/data.csv")

        
