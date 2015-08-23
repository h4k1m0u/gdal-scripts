#!/usr/bin/env python
import numpy as np
from osgeo import gdal

# generate random array (1000x1000) of bytes
arr = np.random.randint(low=0, high=256, size=(1000, 1000))

# initialize geotiff driver
driver = gdal.GetDriverByName('GTiff')
dataset = driver.Create('gdal-random-tiff.tiff', 1000, 1000)

# write image
dataset.GetRasterBand(1).WriteArray(arr)
