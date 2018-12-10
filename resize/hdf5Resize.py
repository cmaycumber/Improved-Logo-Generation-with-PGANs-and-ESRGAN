import h5py
import numpy as np
from PIL import Image
import os, sys
import matplotlib
matplotlib.use("TkAgg")
from matplotlib import pyplot as plt
from tqdm import tqdm
import cv2



dataSet = ('LLD-icon-sharp' if len(sys.argv) is not 2 else sys.argv[1])
hdf5 = dataSet + '.hdf5'
resized = dataSet + 'Resized/'
directoryPath = 'images/' + hdf5
hdf = h5py.File(directoryPath,'r')
images = np.asarray(hdf['data'][:])

mainPath = os.getcwd() + '/'
finalPath = mainPath + "results/" + resized
path = mainPath + directoryPath
final_size = 16 if len(sys.argv) is not 3 else int(sys.argv[2])

def resize_hdf5_images_to_png():
  if not os.path.exists(finalPath):
      os.makedirs(finalPath)

  for i in tqdm( range(len(images)) ):
    img = np.moveaxis(images[i], 0, -1)
    img = cv2.resize(img, dsize=(final_size, final_size), interpolation=cv2.INTER_CUBIC)
    picName = finalPath +  'resized' + str(i) + '.png'
    img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
    cv2.imwrite(picName, img)

resize_hdf5_images_to_png()
