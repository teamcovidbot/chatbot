#!/bin/bash -e
THISDIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
source ${THISDIR}/project_vars.sh

mkdir -p ${CLOUD_FUNCTIONS_DIST_DIR}
pushd ${CLOUD_FUNCTIONS_SRC_DIR} > /dev/null
TIMESTAMP=$(date +"%Y%m%d-%H%M%S")
ZIPFILE=${PROJECTHOME_DIR}/dist/main_${TIMESTAMP}.zip
SRCFILES="main.py"
zip ${ZIPFILE} ${SRCFILES}
unzip -l ${ZIPFILE}
