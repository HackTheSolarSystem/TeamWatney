# PartlyCloudyTeam
TEAM WATNEY
Getting weather data for Watney!

Challenge: Partly Cloudy Skies on Earth and Mars, use OpenSpace's globebrowsing module to visualize weather on Mars and to create a pipeline to get this data from NASA into OpenSpace.

Our solution improves on existing Temporal WMS data pipeline in OpenSpace. We worked with AMNH to host data so anyone can view it immediately. The pipeline we created is general purpose for any planet, any temporal image dataset. Our data flow is a significant improvement from the existing method to get temporal data into OpenSpace. We also added zoom control feature to OpenSpace for flying around space!

The data source used: Mars Color Imager (MARCI) from USGS.gov for daily maps of Martian atmosphere. Images pulled are converted to JPEG using GDAL toolchain.

Our python script converts timestamped images to WMS tile directory, and we created an OpenSpace Temporal Layer XML to show the weather data. 

An intereting issue: some of the satellite data we pulled had was still raw, and it took time to realize these were unprocessed because of the government shutdown. If the government remained shutdown, the servers where we pulled images from would not be working. This presents an interesting issue for open source science: how to handle missing data and prevent against future data gaps.

Members:
Brandon Liu, Alex Kramer, James Somers, Ventrice Lam, Ming Liu, Karoline Dubin
