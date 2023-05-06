#!/bin/bash

configs=("private")

# "gups"
benchmarks=("convolution2d" "fastwalshtransform" "jacobi1d" "jacobi2d" "kmeans" "matrixtranspose" "mis" "pagerank" "simpleconvolution" "shoc-reduction" "spmv" "stencil2d" "syrk" "syr2k")

pgid=`ps -o pgid= $$`
echo "use \`kill -9 -$pgid\` to kill all child processes"

for config in ${configs[@]}; 
do
  for benchmark in ${benchmarks[@]}; 
  do
    echo $config $benchmark
    cd $config
    pwd
    bash ${benchmark}_small.sh > output &
    cd ..
  done
done



        

