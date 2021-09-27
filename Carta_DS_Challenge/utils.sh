#!/usr/bin/env bash

set -x # echo every command
set -e # exit immediately if command returns a nonzero exit value

PY_ENV_DIR='v-env-python3.7'

SCRIPT=$(realpath "$0")
SCRIPT_PATH=$(dirname "${SCRIPT}")
PY_ENV_REQUIREMENTS="${SCRIPT_PATH}/requirements.txt"

# Install Virtual Env
# brew install pipenv

# shellcheck disable=SC2120
create_python_env() {
    PY_ENV_DIR=${1:-'v-env-python3.7'}
    PY_ENV_REQUIREMENTS=${2:-'requirements.txt'}

    if test -d "${PY_ENV_DIR}"; then
        echo "${PY_ENV_DIR} already exists. About to activate existing virtual environment in ${PY_ENV_DIR}"

        # shellcheck disable=SC1090
        source "${PY_ENV_DIR}/bin/activate"
    else
        echo "About to create and activate python 3.7 virtual environment in ${PY_ENV_DIR}"
        python3.7 -m venv "${PY_ENV_DIR}"

        # shellcheck disable=SC1090
        source "${PY_ENV_DIR}/bin/activate"
    fi

    # environment must be activated by now
    if test -f "${PY_ENV_REQUIREMENTS}"; then
        pip install -r "${PY_ENV_REQUIREMENTS}"
    else
        echo "Skipping python virtual env requirements installation because ${PY_ENV_REQUIREMENTS} file does not exist."
    fi
}

# shellcheck disable=SC2119
create_python_env
# shellcheck disable=SC1090
source "${PY_ENV_DIR}/bin/activate"
