import mlflow
import click
import os

def _run(entrypoint, parameters={}, source_version=None, use_cache=True):
    #existing_run = _already_ran(entrypoint, parameters, source_version)
    #if use_cache and existing_run:
    #    print("Found existing run for entrypoint=%s and parameters=%s" % (entrypoint, parameters))
     #   return existing_run
    print("Launching new run for entrypoint=%s and parameters=%s" % (entrypoint, parameters))
    submitted_run = mlflow.run(".", entrypoint, parameters=parameters)
    return mlflow.tracking.MlflowClient().get_run(submitted_run.run_id)


@click.command()
def workflow():
    with mlflow.start_run(run_name ="pystock-training") as active_run:
        mlflow.set_tag("mlflow.runName", "pystock-training")
        train_run = _run("train_model")
        evaluate_run = _run("evaluate_model")        


        model_uri = os.path.join(train_run.info.artifact_uri,"model")
        mlflow.register_model(
           model_uri,
            "training-model-psystock")
              
        print(model_uri)
        #_run("register_model")
        
        
if __name__=="__main__":
    workflow()
