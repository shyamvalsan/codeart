import cv2
import numpy as np
from matplotlib import pyplot as plt
from scipy.misc import imsave
from scipy import ndimage
from scipy import misc
import scipy.misc
import scipy
import image_slicer
from image_slicer import join
from PIL import Image

img = 'arnarstapi.jpg'
num_tiles = 12
tiles = image_slicer.slice(img, num_tiles)
plt.switch_backend('agg')

for tile in tiles:
    img = scipy.misc.imread(tile.filename)
    hist,bins = np.histogram(img.flatten(),256,[0,256])
    cdf = hist.cumsum()
    cdf_normalized = cdf *hist.max()/ cdf.max()  
    plt.plot(cdf_normalized, color = 'g')
    plt.hist(img.flatten(),256,[0,256], color = 'g')
    plt.xlim([0,256])
    plt.legend(('cdf','histogram'), loc = 'upper left')
    cdf_m = np.ma.masked_equal(cdf,0)
    cdf_o = (cdf_m - cdf_m.min())*255/(cdf_m.max()-cdf_m.min())
    cdf = np.ma.filled(cdf_o,0).astype('uint8')
    img3 = cdf[img]
    cv2.imwrite(tile.filename,img3)
    tile.image = Image.open(tile.filename)

image = join(tiles)
image.save('watch-join.png')
