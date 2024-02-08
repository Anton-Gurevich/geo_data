from osgeo import gdal
import numpy as np
import matplotlib.pyplot as plt

if __name__ == '__main__':
    fn = r"C:\Users\e038654\PycharmProjects\geo_data\CH_all.tif"
    ds = gdal.Open(fn)
    print("'ds' type", type(ds))
