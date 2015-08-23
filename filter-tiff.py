#!/usr/bin/env python
import numpy as np
from osgeo import gdal
from scipy.ndimage.filters import median_filter, sobel

# constants
FILEPATH = 'imgs/example.tiff'
FILEPATH_FILTER = 'imgs/example-filter.tiff'

# initialize driver
driver = gdal.GetDriverByName('GTiff')

# read tiff file
dataset = gdal.Open(FILEPATH)

# extract band
band = dataset.GetRasterBand(1)

# extract array from band
arr = band.ReadAsArray()

# write the filtered array
dataset_split = driver.Create(FILEPATH_FILTER , dataset.RasterXSize, dataset.RasterYSize)
dataset_split.GetRasterBand(1).WriteArray(median_filter(arr, size=(5, 5)))
