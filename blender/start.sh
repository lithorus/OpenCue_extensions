#!/bin/bash

BASEPATH=$(realpath  $(dirname $0))

export BLENDER_SYSTEM_SCRIPTS="${BASEPATH}/OpenCueBlender"
export PYTHONPATH="${BASEPATH}:${PYTHONPATH}"

blender --python-use-system-env "$@"
