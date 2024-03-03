import os
from osgeo import gdal, osr
import subprocess
import io

# Set the input and output file paths
input_tiff_path = r'..\data\Ein-Quinia_image.tif'  # Replace with the path to your input GeoTIFF
output_tiff_path = '../data/lla_Ein-Quinia_image.tif'  # Replace with the desired output path

command = f'gdalwarp -t_srs EPSG:4326 -dstnodata None -overwrite "{input_tiff_path}" "{output_tiff_path}" -wo DST_METHOD=NO_GEOTRANSFORM'

subprocess.call(command, shell=True)
