import mlflow
import click

def _run(entrypoint, parameters={}, source_version=None, use_cache=True):
    #existing_run = _already_ran(entrypoint, parameters, source_version)
    #if use_cache and existing_run:
    #    print("Found existing run for entrypoint=%s and parameters=%s" % (entrypoint, parameters))
     #   return existing_run
    print("Launching new run for entrypoint=%s and parameters=%s" % (entrypoint, parameters))
    submitted_run = mlflow.run(".", entrypoint, parameters=parameters)
    return submitted_run


@click.command()
def workflow():
    with mlflow.start_run(run_name ="pystock-data-pipeline") as active_run:
        mlflow.set_tag("mlflow.runName", "pystock-data-pipeline")
        _run("load_raw_data")
        _run("clean_validate_data")
        _run("feature_set_generation")
        
        
if __name__=="__main__":
    workflow()
