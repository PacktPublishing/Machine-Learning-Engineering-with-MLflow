FROM continuumio/miniconda3

RUN pip install mlflow==1.16.0 pandas==1.2.4 protobuf==3.20.*

WORKDIR /batch-scoring/

COPY ./data             /batch-scoring/data
COPY batch_scoring.py   /batch-scoring/
COPY MLproject          /batch-scoring/

ENV MLFLOW_TRACKING_URI=http://localhost:5000

ENTRYPOINT ["mlflow", "run", ".", "--no-conda"]
