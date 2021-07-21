from setuptools import setup, find_packages


setup(
    name="mlflow-psystock-plugin",
    version="0.0.1",
    description="Test plugin for MLflow",
    packages=find_packages(),
    # Require MLflow as a dependency of the plugin, so that plugin users can simply install
    # the plugin & then immediately use it with MLflow
    install_requires=["mlflow"],
    entry_points={
        # Define a MLflow model deployment plugin for target 'psystock'
        "mlflow.deployments": "faketarget=mlflow_psystock_plugin.psystock_deployment_plugin",
    },
)
