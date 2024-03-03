from osgeo import gdal, ogr, osr

# Define the input and output file paths
input_tif = r'../data/Ein-Quinia_elevation.tif'
output_tif = '../data/demo_Ein-Quinia_elevation.tif'
output_tiff_path_to_mem = rf'/vismem/{output_tif}'  # To prevent saving to file

# Define the bounding box coordinates (in EPSG:4326)
xmin, ymin, xmax, ymax = 3925175, 3976284.0 - 3000, 3925175 + 6000, 3976284 + 3000

# Create a tuple with the correct format for the window parameter
window = (ymin, xmax, ymax, xmin)

# Use gdal.Translate to crop the GeoTIFF
_ = gdal.Translate(output_tif, input_tif, projWin=window)

# Close the input dataset
input_ds = None
