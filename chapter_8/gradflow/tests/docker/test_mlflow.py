import mlflow
import pytest
import os


RUN_IDS = {}


@pytest.fixture(scope="module")
def logs():
    parameters = {
        "param1": "param1_val",
        "param2": "param2_val"
    }
    metric = {
        "key": "metric1",
        "step": list(range(10)),
        "val": [i**2 for i in range(10)]
    }
    tag = {
        "key": "tag_key1",
        "val": "tag_val1"
    }

    return {
        "parameters": parameters,
        "metric": metric,
        "tag": tag
    }


@pytest.fixture(scope="module")
def artifact():
    artifact_file = "dummy.txt"
    with open(artifact_file, 'w'):
        pass  # create an empty file

    return artifact_file


def mlflow_start_run(commands):
    experiment_name = 'test_experiment'
    run_name = "test_run"

    mlflow.set_experiment(experiment_name)
    with mlflow.start_run(run_name=run_name) as run:
        commands()
        return run.info.run_id


def mlflow_client():
    return mlflow.tracking.MlflowClient()


def mlflow_get_run(run_id):
    return mlflow_client().get_run(run_id)


@pytest.mark.dependency()
def test_mlflow_log_to_backend(logs):
    # GIVEN
    def mlflow_commands():
        mlflow.log_params(logs["parameters"])

        for ss, vv in zip(logs["metric"]["step"], logs["metric"]["val"]):
            mlflow.log_metric(logs["metric"]["key"], vv, step=ss)

        mlflow.set_tag(logs["tag"]["key"], logs["tag"]["val"])

    # WHEN
    RUN_IDS["test_mlflow_log_to_backend"] = mlflow_start_run(mlflow_commands)

    # THEN
    assert True  # logging succeeded


@pytest.mark.dependency(depends=["test_mlflow_log_to_backend"])
def test_mlflow_get_params(logs):
    # GIVEN 
    run_id = RUN_IDS["test_mlflow_log_to_backend"]

    # WHEN
    data = mlflow_get_run(run_id).data

    #THEN
    assert data.params == logs["parameters"]


@pytest.mark.dependency(depends=["test_mlflow_log_to_backend"])
def test_mlflow_get_metric(logs):
    # GIVEN 
    run_id = RUN_IDS["test_mlflow_log_to_backend"]

    # WHEN
    metric = mlflow_client().get_metric_history(run_id, logs["metric"]["key"])
    metric_vals = [mm.value for mm in metric]
    metric_steps = [mm.step for mm in metric]

    #THEN
    assert (metric_vals == logs["metric"]["val"]) and (metric_steps == logs["metric"]["step"])


@pytest.mark.dependency()
def test_mlflow_log_artifact(artifact):
    # GIVEN
    def mlflow_commands():
        mlflow.log_artifact(artifact)

    # WHEN
    RUN_IDS["test_mlflow_log_artifact"] = mlflow_start_run(mlflow_commands)

    # THEN
    assert True  # logging succeeded


@pytest.mark.dependency(depends=["test_mlflow_log_artifact"])
def test_mlflow_get_artifact(artifact):
    # GIVEN 
    run_id = RUN_IDS["test_mlflow_log_artifact"]

    # WHEN
    artifact_dir = mlflow_get_run(run_id).info.artifact_uri
    artifact_file = os.path.join(artifact_dir, artifact)

    #THEN
    assert os.path.isfile(artifact_file)
