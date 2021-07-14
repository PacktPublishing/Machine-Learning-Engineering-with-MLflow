FROM continuumio/miniconda3

WORKDIR /batch-scoring/

RUN pip install mlflow==1.16.0

RUN pip install pandas==1.2.4

COPY batch_scoring.py   /batch-scoring/
COPY MLproject          /batch-scoring/

ENV MLFLOW_TRACKING_URI=http://localhost:5000

ENTRYPOINT ["mlflow run . --no-conda"]
