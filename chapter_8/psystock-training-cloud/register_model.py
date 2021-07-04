import mlflow

if __name__ == "__main__":
    
    with mlflow.start_run(run_name="register_model") as run:

        mlflow.set_tag("mlflow.runName", "register_model")

        result = mlflow.register_model(
           "runs:/ae1a3226f71d4c029a2504feca232a35/artifacts/model",
            "training-model-psystock")
        