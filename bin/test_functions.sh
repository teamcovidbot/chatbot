#!/bin/bash -e
THISDIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
source ${THISDIR}/project_vars.sh

export COMMAND="$@"
if [[ $# -eq 0 ]] ; then
    export COMMAND="pytest -vv"
fi

docker run \
  --rm \
  --tty --interactive \
  -v $PWD:$PWD \
  -w $PROJECTHOME_DIR \
  -e PYTHONPATH=.:$PWD \
  --name ${CLOUD_FUNCTIONS_HOSTNAME} \
  ${CLOUD_FUNCTIONS_IMAGE_TAG} $COMMAND
