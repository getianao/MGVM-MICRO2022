#!/bin/bash

fullpath=$(readlink --canonicalize --no-newline $BASH_SOURCE)
cur_dir=$(cd `dirname ${fullpath}`; pwd)
echo ${cur_dir}


./0_clean.sh
./1_compile_benchmarks.py 
./2_copy_benchmarks.sh 
./3_gen_runners.py
./3_gen_runners_small.py