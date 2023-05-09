#!/bin/bash

#BSUB -q lmem

#BSUB -n 56

#BSUB -e error.%J

#BSUB -o output.%J

#BSUB -W 48:00

#BSUB -J mgpusim

fullpath=$(readlink --canonicalize --no-newline $BASH_SOURCE)
cur_dir=$(cd `dirname ${fullpath}`; pwd)
echo ${cur_dir}


# bsub -q lmem -n 16 -e error.%J -o output.%J -W 48:00 -J mgpusim -M
./4_run_benchmarks_private.sh &
./4_run_benchmarks_private-ideal.sh &
./4_run_benchmarks_shared.sh &
# ./4_run_benchmarks_shared-h1.sh &
# ./4_run_benchmarks_mgvm-nobalance.sh &
./4_run_benchmarks_xortlb-ideal1.sh &
./4_run_benchmarks_mgvm.sh &
./4_run_benchmarks_mgvm-ideal1.sh &


wait