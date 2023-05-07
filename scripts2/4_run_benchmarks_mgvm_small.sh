#!/bin/bash

configs=("mgvm")

# "gups"
benchmarks=("convolution2d" "fastwalshtransform"  "jacobi1d" "jacobi2d" "kmeans" "matrixtranspose" "mis" "pagerank" "simpleconvolution" "shoc-reduction" "spmv" "stencil2d" "syrk" "syr2k")

pgid=`ps -o pgid= $$|sed 's/ //g'`
echo "use \`kill -9 -$pgid\` to kill all child processes"

for config in ${configs[@]}; 
do
  mkdir -p ./$config/log
  for benchmark in ${benchmarks[@]}; 
  do
    echo $config $benchmark
    cd $config
    # pwd
    bash ${benchmark}_small.sh > log/${benchmark}_small.log &
    cd ..
  done
done

wait
        

