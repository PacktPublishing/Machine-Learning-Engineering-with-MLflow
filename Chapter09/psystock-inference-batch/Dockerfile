FROM continuumio/miniconda3

WORKDIR /batch-scoring/

RUN pip install mlflow
COPY ./   /batch-scoring/

ENV MLFLOW_TRACKING_URI=http://172.31.29.157:5000

ENTRYPOINT ["mlflow", "run", "."]
