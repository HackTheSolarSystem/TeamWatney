gdal_translate -of GTiff -a_ullr -180 90 180 -90 -a_srs EPSG:4326 B20_day01_resx2.tiff output.tif
gdalbuildvrt hackathon.vrt *.tif
