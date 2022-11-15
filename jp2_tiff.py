import rasterio

path = "./images/"

files = [
    path + "B02.jp2",  # Blue
    path + "B03.jp2",  # Green
    path + "B04.jp2",  # Red
    path + "B08.jp2"   # NIR
]

src = rasterio.open(files[0])
meta = src.meta
meta.update(count=len(files))
meta.update(driver="GTiff")

with rasterio.open("output/sentinel2.tif", "w", **meta) as dst:
    for id, layer in enumerate(files, start=1):
        with rasterio.open(layer) as src:
            dst.write(src.read(1), id)
