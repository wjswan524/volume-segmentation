# -*- coding: utf-8 -*-
"""
Created on Thu Jan  9 11:32:08 2020

@author: wjswan524
"""

import numpy as np
from skimage import segmentation as seg

segs = seg.morphological_chan_vese(volred, iterations=3, init_level_set='checkerboard',smoothing=1)

segred = np.zeros((713,642,924))
for i in range(713):
    for j in range(642):
        for k in range(924):
            segred[i,j,k] = segs[i,j,(k+20)]
        
    

pores = 0.
solid = 0.

for i in range(713):
    for j in range(642):
        for k in range(924):
            if segred[i,j,k] == 0:
                pores += 1.
            elif segred[i,j,k] == 1:
                solid += 1.
            
        
    

total = pores + solid
porosity = pores / total