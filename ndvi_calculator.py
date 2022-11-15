import numpy
import rasterio
from rasterio import plot
import matplotlib.pyplot as plt


image_file = "./output/sentinel2.tif"

with rasterio.open(image_file) as src:
    band_red = src.read(3)
    band_nir = src.read(4)


# Allow division by zero
numpy.seterr(divide='ignore', invalid='ignore')

# # Calculate NDVI
ndvi = (band_nir.astype(float) - band_red.astype(float)) / (band_nir + band_red)


# Set spatial characteristics of the output object to mirror the input
kwargs = src.meta
kwargs.update(
    dtype=rasterio.float32,
    count=1,
    )

# Create the file
with rasterio.open('./result/2ndvi.tiff', 'w', **kwargs) as dst:
    dst.write_band(1, ndvi.astype(rasterio.float32))

with rasterio.open('./result/2ndvi.tiff') as result:
    fig = plt.figure(figsize=(18, 12))
    plot.show(result)
