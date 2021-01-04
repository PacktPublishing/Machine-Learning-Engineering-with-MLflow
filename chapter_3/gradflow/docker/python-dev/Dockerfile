FROM python:3.7-slim

# install git; needed for pip if the repo has git dependencies
RUN apt-get update && \
    apt-get install -y --no-install-recommends git && \
    apt-get purge -y --auto-remove && \
    rm -rf /var/lib/apt/lists/*

COPY docker/python-dev/requirements.txt /install/
RUN pip install -r /install/requirements.txt && \
    rm -rf /install

COPY ./ /repo/
WORKDIR /repo/
CMD ["tox"]
