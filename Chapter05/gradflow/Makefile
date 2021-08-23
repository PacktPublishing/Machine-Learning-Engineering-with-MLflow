SHELL := /bin/bash
.DEFAULT_GOAL := default
.PHONY: \
	help default lab notebook \
	scipy tensorflow pyspark \
	test test-store-permissions all \
	purge clean clean-all clean-stores clean-python \
	prune build \
	up run down down-all \
	python-dev-build tox \
	sphinx-build sphinx-clean sphinx-apidoc sphinx-html sphinx-html-test \
	free-port debug-travis

HELP_PADDING = 28
bold := $(shell tput bold)
sgr0 := $(shell tput sgr0)
padded_str := %-$(HELP_PADDING)s
pretty_command := $(bold)$(padded_str)$(sgr0)

include .env  # environment variables used in docker-compose stack

export

MAKEFILE_DIR = $(dir $(realpath $(firstword $(MAKEFILE_LIST))))

PRUNE_OPTS = -f

BUILDKIT = 1
BUILD_OPTS = 

DOWN_OPTS = --remove-orphans
DOWN_ALL_OPTS = ${DOWN_OPTS} --rmi all -v

UP_OPTS =
RUN_OPTS =

PYTHON_DEV_CMD =

DOCS_FOLDER = docs
SPHINX_OPTS := -nWT -b linkcheck --keep-going

PORT = ${POSTGRES_PORT}

HOST_USERNAME := $(shell id -u -n)

JUPYTER_BASE_IMAGE := ${JUPYTER_SCIPY_IMAGE}
JUPYTER_BASE_VERSION := ${JUPYTER_SCIPY_VERSION}

JUPYTER_CHOWN_EXTRA := "/${DATA_DIR}"
JUPYTER_UID := $(shell id -u)
JUPYTER_USERNAME := $(shell id -u -n)

POSTGRES_UID := $(shell id -u)
POSTGRES_GID := $(shell id -g)

TRAVIS_JOB =
TRAVIS_TOKEN =


default: clean build up
lab: default

notebook: JUPYTER_ENABLE_LAB:=
notebook: default

scipy: JUPYTER_BASE_IMAGE=${JUPYTER_SCIPY_IMAGE}
scipy: JUPYTER_BASE_VERSION=${JUPYTER_SCIPY_VERSION}
scipy: default

tensorflow: JUPYTER_BASE_IMAGE=${JUPYTER_TENSORFLOW_IMAGE}
tensorflow: JUPYTER_BASE_VERSION=${JUPYTER_TENSORFLOW_VERSION}
tensorflow: default

pyspark: JUPYTER_BASE_IMAGE=${JUPYTER_PYSPARK_IMAGE}
pyspark: JUPYTER_BASE_VERSION=${JUPYTER_PYSPARK_VERSION}
pyspark: default

test: JUPYTER_TARGET:=${JUPYTER_TEST_TARGET}
test: RUN_OPTS:=jupyter start.sh ./run_docker_tests.sh ${MLFLOW_IMAGE_NAME} ${MLFLOW_TRACKING_SERVER_PORT} ${WAIT_FOR_IT_TIMEOUT}
test: JUPYTER_CHOWN_EXTRA:="/${DATA_DIR},/tests"
test: clean build run test-store-permissions
	$(MAKE) down
# NOTE: above, `clean` had already called `down` so we had to make
# an explicit recursive call by `$(MAKE) down` 

test-store-permissions:
	@if [ $(shell find data ! -user ${HOST_USERNAME} | wc -l) -gt 0 ]; then \
		echo "Found files and/or folders with wrong permission: " ; \
		echo "=> $(shell find data ! -user ${HOST_USERNAME} -printf '%p (%u) ')" ; \
		exit 1 ; \
	else \
		exit 0 ; \
	fi

all: clean clean-stores build up

purge: clean-all
clean-all: down-all prune clean-stores clean-python
clean: down prune
clean-stores:
	rm -rf ./${MLFLOW_ARTIFACT_STORE} ./${POSTGRES_STORE}

clean-python:
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -fr {} +
	find . -name '.ipynb_checkpoints' -exec rm -fr {} +
	rm -rf build/
	rm -rf dist/
	rm -rf .eggs/
	rm -rf .pytest_cache
	find . -name '.eggs' -type d -exec rm -rf {} +
	find . -name '*.egg-info' -exec rm -rf {} +
	find . -name '*.egg' -exec rm -f {} +
	rm -fr .tox/
	rm -f .coverage
	rm -fr htmlcov/

prune:
	docker system prune ${PRUNE_OPTS}

build:
	DOCKER_BUILDKIT=${BUILDKIT} COMPOSE_DOCKER_CLI_BUILD=${BUILDKIT} \
	JUPYTER_BASE_IMAGE=${JUPYTER_BASE_IMAGE} JUPYTER_BASE_VERSION=${JUPYTER_BASE_VERSION} \
	JUPYTER_TARGET=${JUPYTER_TARGET} JUPYTER_USERNAME=${JUPYTER_USERNAME} \
	MLFLOW_VERSION=${MLFLOW_VERSION} \
	POSTGRES_UID=${POSTGRES_UID} POSTGRES_GID=${POSTGRES_GID} \
	docker-compose build ${BUILD_OPTS}

${MLFLOW_ARTIFACT_STORE}:
	mkdir -p ${MLFLOW_ARTIFACT_STORE}

${POSTGRES_STORE}:
	mkdir -p ${POSTGRES_STORE}

up: ${MLFLOW_ARTIFACT_STORE} ${POSTGRES_STORE}
	JUPYTER_BASE_IMAGE=${JUPYTER_BASE_IMAGE} JUPYTER_BASE_VERSION=${JUPYTER_BASE_VERSION} \
	JUPYTER_TARGET=${JUPYTER_TARGET} \
	JUPYTER_CHOWN_EXTRA=${JUPYTER_CHOWN_EXTRA} \
	JUPYTER_UID=${JUPYTER_UID} JUPYTER_USERNAME=${JUPYTER_USERNAME} \
	JUPYTER_ENABLE_LAB=${JUPYTER_ENABLE_LAB} \
	POSTGRES_UID=${POSTGRES_UID} POSTGRES_GID=${POSTGRES_GID} \
	docker-compose up ${UP_OPTS}

run: ${MLFLOW_ARTIFACT_STORE} ${POSTGRES_STORE}
	JUPYTER_BASE_IMAGE=${JUPYTER_BASE_IMAGE} JUPYTER_BASE_VERSION=${JUPYTER_BASE_VERSION} \
	JUPYTER_TARGET=${JUPYTER_TARGET} \
	JUPYTER_CHOWN_EXTRA=${JUPYTER_CHOWN_EXTRA} \
	JUPYTER_UID=${JUPYTER_UID} JUPYTER_USERNAME=${JUPYTER_USERNAME} \
	JUPYTER_ENABLE_LAB=${JUPYTER_ENABLE_LAB} \
	POSTGRES_UID=${POSTGRES_UID} POSTGRES_GID=${POSTGRES_GID} \
	docker-compose run ${RUN_OPTS}

down:
	docker-compose down ${DOWN_OPTS}
down-all: DOWN_OPTS:=${DOWN_ALL_OPTS}
down-all: down

python-dev-build:	
	DOCKER_BUILDKIT=${BUILDKIT} \
	docker build . \
		-f ./docker/python-dev/Dockerfile \
		-t ${IMAGE_OWNER}/${PYTHON_DEV_IMAGE_NAME}:${VERSION} \
		${BUILD_OPTS}

tox: PYTHON_DEV_CMD := tox
tox: python-dev-build
	docker run -it ${IMAGE_OWNER}/${PYTHON_DEV_IMAGE_NAME}:${VERSION} ${PYTHON_DEV_CMD}



