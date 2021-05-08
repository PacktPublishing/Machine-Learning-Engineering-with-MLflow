import pandas as pd
import mlflow
import xgboost as xgb
import mlflow.xgboost
from sklearn.model_selection import train_test_split

def train_test_split_pandas(pandas_df,t_size=0.33,r_tate=42):
    X=pandas_df.iloc[:,:-1]
    Y=pandas_df.iloc[:,-1]
    X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=t_size, random_state=r_tate)

    return X_train, X_test, y_train, y_test

if __name__ == "__main__":

    THRESHOLD = 0.5

    mlflow.xgboost.autolog()
    with mlflow.start_run(run_name="train_model") as run:
        mlflow.set_tag("mlflow.runName", "train_model")

        pandas_df=pd.read_csv("data/training/data.csv", header=None)

        X_train, X_test, y_train, y_test = train_test_split_pandas(pandas_df)

        train_data = xgb.DMatrix(X_train, label=y_train)
        test_data =  xgb.DMatrix(X_test)

        model = xgb.train(dtrain=train_data,params={})
        
        y_probas=model.predict(test_data) 
        y_preds = [1 if  y_proba > THRESHOLD else 0. for y_proba in y_probas]

        test_prediction_results = pd.DataFrame(data={'y_pred':y_preds,'y_test':y_test})

        result = test_prediction_results
        
        result.to_csv("data/predictions/test_predictions.csv")