#!/bin/bash

fullpath=$(readlink --canonicalize --no-newline $BASH_SOURCE)
cur_dir=$(cd `dirname ${fullpath}`; pwd)
echo ${cur_dir}

# ./4_run_benchmarks_shared_small.sh
# ./4_run_benchmarks_private_small.sh
# ./4_run_benchmarks_mgvm-nobalance_small.sh
# ./4_run_benchmarks_mgvm_small.sh
