#!/bin/bash

read length

array=()

for ((i=0;i<$length;i++))
do
    array+=("0")
done

for element in "${array[@]}"
do
    echo "$element"
done 