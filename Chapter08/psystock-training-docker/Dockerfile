FROM continuumio/miniconda3:4.9.2

RUN apt-get update --allow-releaseinfo-change && apt-get install build-essential -y
RUN pip install \
    mlflow==1.18.0 \
    psycopg2-binary \
    boto3

ENV MLFLOW_TRACKING_URI=http://172.31.29.157:5000

COPY ./training_project /src

WORKDIR /src


ENTRYPOINT ["mlflow", "run", "."]


