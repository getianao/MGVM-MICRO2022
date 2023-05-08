#!/bin/bash

configs=("xortlb-ideal1")

benchmarks=("convolution2d" "fastwalshtransform" "gups" "jacobi1d" "jacobi2d" "kmeans" "matrixtranspose" "mis" "pagerank" "simpleconvolution" "shoc-reduction" "spmv" "stencil2d" "syrk" "syr2k")

pgid=`ps -o pgid= $$`
echo "use \`kill -9 -$pgid\` to kill all child processes"

for config in ${configs[@]}; 
do
  mkdir -p ./$config/log
  for benchmark in ${benchmarks[@]}; 
  do
    echo $config $benchmark
    cd $config
    # pwd
    bash ${benchmark}.sh > log/${benchmark}.log &
    cd ..
  done
done
        

wait