from osgeo import gdal
import numpy as np

def read_band_as_array(dataset, band_number):
    # Get the specified band
    band = dataset.GetRasterBand(band_number)

    # Read the band data as a NumPy array
    band_array = band.ReadAsArray()

    return band_array


def resample_raster(input_raster, output_raster_path, target_pixel_width, target_pixel_height):
    # target_pixel_width, target_pixel_height in degrees!!!
    # Get the existing geotransform and other properties from the input raster
    geotransform = input_raster.GetGeoTransform()
    projection = input_raster.GetProjection()

    # Calculate the new dimensions
    new_width = int(input_raster.RasterXSize * (geotransform[1] / target_pixel_width))
    new_height = int(input_raster.RasterYSize * (geotransform[5] / target_pixel_height))

    # Create a new raster dataset with the target pixel size
    output_dataset = gdal.GetDriverByName('GTiff').Create(output_raster_path, new_width, new_height,
                                                          input_raster.RasterCount, input_raster.GetRasterBand(1).DataType)

    # Set the new geotransform
    output_geotransform = (geotransform[0], target_pixel_width, 0, geotransform[3], 0, target_pixel_height)
    output_dataset.SetGeoTransform(output_geotransform)

    # Set the projection
    output_dataset.SetProjection(projection)

    # Perform resampling
    gdal.ReprojectImage(input_raster, output_dataset, input_raster.GetProjection(), output_dataset.GetProjection(),
                        gdal.GRA_Bilinear)

    return output_dataset


if __name__ == "__main__":
    output_path = r'\vsimem\out.tif'
    # raster_path = r'C:\Users\e038654\PycharmProjects\geo_data\data\Ein-Quinia_image.tif'
    raster_path = r'C:\Users\e038654\PycharmProjects\geo_data\data\Ein-Quinia_image.tif'
    dataset = gdal.Open(raster_path)
    Transform = dataset.GetGeoTransform()

    # Specify the band number (e.g., 1 for the first band)
    band_number = 1

    # Read the band as a NumPy array
    band_array = read_band_as_array(dataset, band_number)

    # Now, 'band_array' contains the pixel values of the specified band as a NumPy array
    print(band_array.shape)

    target_pixel_width = Transform[1] * 1.25
    target_pixel_height = Transform[5] * 1.25

    resample_raster = resample_raster(dataset, output_path, target_pixel_width, target_pixel_height)

    # Close the dataset
    dataset = None
