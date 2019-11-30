# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 09:30:30 2019

A script to construct a 3-D array of dimensions (i,j,k) where (i,j) is the
shape of the numpy array corresponding to each image and k is the total number
of images in the directory for the micro-CT scan being used.

One limitation of this approach is that it requires the target directory to be
cleared of extraneous files. Alternatively, the target files may be copied to
a clean directory.
"""

import numpy as np
import os
import imageio
import skimage

os.chdir('C:/Users/wjswa/Documents/Micro-CT scans/81/')

asdf = np.zeros((1013,992,994))

files = os.listdir()

for k in range(len(files)):
    im = imageio.imread(files[k])
    img = np.asarray(im)
    bw = skimage.color.rgb2gray(img)
    asdf[:,:,k] = bw

img450 = asdf[:,:,450]