#!/bin/bash

fullpath=$(readlink --canonicalize --no-newline $BASH_SOURCE)
cur_dir=$(cd `dirname ${fullpath}`; pwd)
echo ${cur_dir}

python 5_collect_stats.py
python 6_normalize_results.py results.csv normalized.csv