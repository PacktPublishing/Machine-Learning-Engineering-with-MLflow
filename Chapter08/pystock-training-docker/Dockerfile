FROM continuumio/miniconda3:4.9.2

RUN apt-get update && apt-get install build-essential -y

RUN pip install \
    mlflow==1.18.0 \
    pymysql==1.0.2 \
    boto3

COPY ./training_project /src

WORKDIR /src


ENTRYPOINT ["mlflow", "run", "."]


