#!/bin/bash -e
THISDIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
source ${THISDIR}/project_vars.sh
docker build \
  --tag ${CLOUD_FUNCTIONS_IMAGE_TAG} \
  ${CLOUD_FUNCTIONS_DOCKER_DIR}
