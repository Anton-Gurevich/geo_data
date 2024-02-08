from osgeo import gdal, ogr, osr

# Define the input and output file paths
input_tif = r'C:\Users\e038654\PycharmProjects\geo_data\lla_CH_all.tif'
output_tif = 'cropp.tif'

# Define the bounding box coordinates (in EPSG:4326)
xmin, ymin, xmax, ymax = 46.94436, 8.27436, 46.97729, 8.33900

# Create a tuple with the correct format for the window parameter
window = (ymin, xmax, ymax, xmin)


# Use gdal.Translate to crop the GeoTIFF
aa = gdal.Translate(output_tif, input_tif, projWin=window)

# Close the input dataset
input_ds = None
