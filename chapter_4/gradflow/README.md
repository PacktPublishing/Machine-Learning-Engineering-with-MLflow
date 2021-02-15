# workbench

A template workbench.

This workbench is based on a  "cut" from [sertansenturk/cookiecutter-ds-docker](https://github.com/sertansenturk/cookiecutter-ds-docker).


## 1. Introduction


It consists of a docker-compose stack with the services below (See Sections [Setup](#setup) and [Running the Services](#running-the-services)):

1. A [Jupyter](https://jupyter.org/) service with minimal customization
2. An [mlflow](https://mlflow.org/) tracking server to store experiments
3. A [postgresql](https://www.postgresql.org/) database, which stores mlflow tracking information

`workbench` also comes with two standalone *Docker* image below for local usage:

1. *Python* test and development
2. Building *Sphinx* documentation


## 3. Quickstart

To build and start the Docker stack, run:

```bash
make
