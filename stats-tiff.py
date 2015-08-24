#!/usr/bin/env python
import numpy as np
from osgeo import gdal
from scipy.ndimage.measurements import *

# constants
FILEPATH = 'imgs/example.tiff'

# initialize driver
driver = gdal.GetDriverByName('GTiff')

# read tiff file
dataset = gdal.Open(FILEPATH)

# extract band
band = dataset.GetRasterBand(1)

# extract array from band
arr = band.ReadAsArray()

# get stats (mean, variance, std_dev...) about image array
print 'Min:', minimum(arr)
print 'Max:', maximum(arr)
print 'Mean:', mean(arr)
print 'Variance:', variance(arr)
print 'Standard deviation:', standard_deviation(arr)
