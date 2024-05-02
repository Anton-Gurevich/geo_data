import rasterio
from rasterio.warp import calculate_default_transform, reproject, Resampling


def reproject_raster(input_path, output_path, new_crs='EPSG:4326'):
    with rasterio.open(input_path) as src:
        transform, width, height = calculate_default_transform(
            src.crs, new_crs, src.width, src.height, *src.bounds)
        kwargs = src.meta.copy()
        kwargs.update({
            'crs': new_crs,
            'transform': transform,
            'width': width,
            'height': height
        })

        with rasterio.open(output_path, 'w', **kwargs) as dst:
            for i in range(1, src.count + 1):
                reproject(
                    source=rasterio.band(src, i),
                    destination=rasterio.band(dst, i),
                    src_transform=src.transform,
                    src_crs=src.crs,
                    dst_transform=transform,
                    dst_crs=new_crs,
                    resampling=Resampling.nearest)


reproject_raster('/home/algo/PycharmProjects/geo_data/data/Ramot_Menashe_1.0m_24bit.tif',
                 '/home/algo/PycharmProjects/geo_data/data/Ramot_Menashe_1.0m_24bit_EPSG4326.tif')