#!/bin/bash

mkdir -p raw

for value in $(seq -f "%02g" 1 33)
do
    (cd ./raw && curl -O https://pdsimage2.wr.usgs.gov/downloads/MARCI/data_B20/data_resx2/color/B20_day${value}_resx2.tiff)
done
