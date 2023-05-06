#!/bin/bash

fullpath=$(readlink --canonicalize --no-newline $BASH_SOURCE)
cur_dir=$(cd `dirname ${fullpath}`; pwd)
echo ${cur_dir}

export PROJECT_ROOT=${cur_dir}

export PATH="${PROJECT_ROOT}/bin:${PATH}"
