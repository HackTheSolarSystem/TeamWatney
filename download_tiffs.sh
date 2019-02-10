#!/bin/bash

mkdir -p sources
cd sources

for batch in $(seq -f "%02g" 1 20)
do
  seq -f "%02g" 1 33 | parallel -j10 wget -q https://pdsimage2.wr.usgs.gov/downloads/MARCI/data_B${batch}/data_resx2/color/B${batch}_day{1}_resx2.tiff
done
