#!/usr/bin/env python
import numpy as np
from osgeo import gdal

# constants
FILENAME = 's1a-iw-grd-vv-20150823t070201-20150823t070226-007387-00a28a-001.tiff'
SPLIT_SIZE = 1000

# initialize driver
driver = gdal.GetDriverByName('GTiff')

# read tiff file
dataset = gdal.Open(FILENAME)

# extract band
band = dataset.GetRasterBand(1)

# extract splits iteratively
y_offset = 0
while y_offset + SPLIT_SIZE < dataset.RasterYSize:
    x_offset = 0
    while x_offset + SPLIT_SIZE < dataset.RasterXSize:
        arr = band.ReadAsArray(x_offset, y_offset, SPLIT_SIZE, SPLIT_SIZE)

        # write the split to a separate file
        file_path = 'splits/gdal-split-[%s,%s].tiff' % (x_offset, y_offset)
        dataset_split = driver.Create(file_path, SPLIT_SIZE, SPLIT_SIZE)
        dataset_split.GetRasterBand(1).WriteArray(arr)

        # next split
        print file_path, 'saved.'
        x_offset += SPLIT_SIZE

    y_offset += SPLIT_SIZE
