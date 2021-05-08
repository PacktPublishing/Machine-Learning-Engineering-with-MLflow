import pandas as pd
import mlflow
import mlflow.pyfunc

if __name__ == "__main__":

    with mlflow.start_run(run_name="batch_scoring") as run:

        data=pd.read_csv("data/input.csv",header=None)

        model_name = "training-model-psystock"
        stage = 'Production'

        model = mlflow.pyfunc.load_model(
                model_uri=f"models:/{model_name}/{stage}"
        )

        y_probas=model.predict(data)

        y_preds = [1 if  y_proba > 0.5 else 0 for y_proba in y_probas]
        
        data[len(data.columns)] =y_preds
        
        result = data

        result.to_csv("data/output.csv")
