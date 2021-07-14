import ray
from ray import serve

import mlflow.pyfunc


class MLflowBackend:
    def __init__(self, model_uri):
        self.model = mlflow.pyfunc.load_model(model_uri=model_uri)

    async def __call__(self, request):
        return self.model.predict(request.data)


ray.init()
client = serve.start()
# This can be the same checkpoint that was saved by MLflow Tracking
model_uri = "/Users/ray_user/my_mlflow_model"
# Or you can load a model from the MLflow model registry
model_uri = "model:/my_registered_model/Production"
client.create_backend("mlflow_backend", MLflowBackend, model_uri)
