#!/usr/bin/env python
import numpy as np
import matplotlib.pyplot as plt
from osgeo import gdal

# constants
FILEPATH = 'imgs/example.tiff'
FILEPATH_FILTER = 'imgs/example-filter.tiff'

# read img file inside array
dataset = gdal.Open(FILEPATH)
band = dataset.GetRasterBand(1)
arr = band.ReadAsArray()

# plot histogram
plt.hist(arr)
plt.show()
