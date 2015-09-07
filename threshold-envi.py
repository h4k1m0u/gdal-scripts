#!/usr/bin/env python
import numpy as np
from osgeo import gdal
import sys

# check if required arguments are provided
if len(sys.argv) < 3:
    print 'Product file and Threshold value required'
    sys.exit(1)

# files paths constants
FILEPATH = sys.argv[1]
FILEPATH_FILTERED = 'imgs/thresholded.img'

# read 'single band' file & extract array from the band
dataset = gdal.Open(FILEPATH)
band = dataset.GetRasterBand(1)
arr = band.ReadAsArray()

# write the thresholded array in envi format
threshold_value = int(sys.argv[2])
driver = gdal.GetDriverByName('ENVI')
dataset_split = driver.Create(FILEPATH_FILTERED, dataset.RasterXSize, dataset.RasterYSize)
dataset_split.GetRasterBand(1).WriteArray(arr > threshold_value)
