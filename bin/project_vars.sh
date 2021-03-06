#!/bin/bash
export PROJECTHOME_DIR=$(git rev-parse --show-toplevel)
export PROJECT_NAME=${PROJECTHOME_DIR##/*/}

export CLOUD_FUNCTIONS_IMAGE_TAG=${PROJECT_NAME}-functions
export CLOUD_FUNCTIONS_HOSTNAME=cloud_functions
export CLOUD_FUNCTIONS_DOCKER_DIR=${PROJECTHOME_DIR}/docker
export CLOUD_FUNCTIONS_SRC_DIR=${PROJECTHOME_DIR}/cloud_functions
export CLOUD_FUNCTIONS_DIST_DIR=${PROJECTHOME_DIR}/dist
