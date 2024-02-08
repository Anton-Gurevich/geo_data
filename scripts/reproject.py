import os
from osgeo import gdal, osr
import subprocess
import io

# Set the input and output file paths
input_tiff_path = r'C:\Users\e038654\PycharmProjects\geo_data\CH_all.tif'  # Replace with the path to your input GeoTIFF
output_tiff_path = '../data/lla_CH_all.tif'  # Replace with the desired output path
output_tiff_path_to_mem = f'/vismem/{output_tiff_path}'  # Replace with the desired output path

command = f'gdalwarp -t_srs EPSG:4326 -dstnodata None -overwrite "{input_tiff_path}" "{output_tiff_path}" -wo DST_METHOD=NO_GEOTRANSFORM'
print()

subprocess.call(command, shell=True)
