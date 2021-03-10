#!/bin/bash
set -e

echo "Testing if workbench is installed in editable mode"
ls /opt/conda/lib/python3.7/site-packages/workbench.egg-link

./wait-for-it.sh $1:$2 -t $3 -- \
    echo "Running pytest as $USER with uid $UID" && \
    pytest -vv "$(pwd)/docker"
