FROM python:3.7

EXPOSE 5000

ARG MLFLOW_VERSION
ARG SERVER_DIR=/server

RUN pip install mlflow==$MLFLOW_VERSION psycopg2==2.8.* && \
    mkdir -p ${SERVER_DIR}

COPY ./scripts/wait-for-it.sh ${SERVER_DIR}/
RUN chmod +x ${SERVER_DIR}/wait-for-it.sh

WORKDIR ${SERVER_DIR}

# wait as long as 60 seconds for posgres to init db, which takes a lot of time particularly in mac osx
CMD ./wait-for-it.sh ${MLFLOW_BACKEND_STORE}:${POSTGRES_PORT} -t ${WAIT_FOR_IT_TIMEOUT} -- \
    mlflow server \
    --backend-store-uri postgresql://${POSTGRES_USER}:${POSTGRES_PASSWORD}@${MLFLOW_BACKEND_STORE}:${POSTGRES_PORT}/${POSTGRES_DATABASE} \
    --default-artifact-root /${MLFLOW_ARTIFACT_STORE} \
    --host ${MLFLOW_TRACKING_SERVER_HOST} \
    --port ${MLFLOW_TRACKING_SERVER_PORT}
