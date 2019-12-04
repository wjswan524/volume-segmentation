# -*- coding: utf-8 -*-
"""
Combined code from nbhd.py and grow.py, both of which are built directly from 
code on the personal blog of Matt Hancock, < notmatthancock.github.io >, to 
whom all credit is due.
"""

import numpy as np

def get_nbhd(pt, checked, dims):
    nbhd = []
    
    if (pt[0] > 0) and not checked[pt[0]-1, pt[1], pt[2]]:
        nbhd.append((pt[0]-1, pt[1], pt[2]))
    if (pt[1] > 0) and not checked[pt[0], pt[1]-1, pt[2]]:
        nbhd.append((pt[0], pt[1]-1, pt[2]))
    if (pt[2] > 0) and not checked[pt[0], pt[1], pt[2]-1]:
        nbhd.append((pt[0], pt[1], pt[2]-1))
    
    if (pt[0] < dims[0]-1) and not checked[pt[0]+1, pt[1], pt[2]]:
        nbhd.append((pt[0]+1, pt[1], pt[2]))
    if (pt[1] < dims[1]-1) and not checked[pt[0], pt[1]+1, pt[2]]:
        nbhd.append((pt[0], pt[1]+1, pt[2]))
    if (pt[2] < dims[2]-1) and not checked[pt[0], pt[1], pt[2]+1]:
        nbhd.append((pt[0], pt[1], pt[2]+1))
    
    return nbhd


def grow(img,seed,t):
    '''
    img: ndarray, ndim=3
        Image volume from 2-D slices
    seed: tuple, len=3
        Starting coordinate for region growing
    t: int
        Neighborhood radius (in voxels) for inclusion criteria
    '''
    seg = np.zeros(img.shape, dtype=np.bool)
    checked = np.zeros_like(seg)
    
    seg[seed] = True
    checked[seed] = True
    needs_check = get_nbhd(seed,checked,img.shape)
    
    while len(needs_check) > 0:
        pt = needs_check.pop()
        if checked[pt]: continue
        checked[pt] = True
        
        imin = max([pt[0]-t,0])
        imax = min(pt[0]+t,img.shape[0]-1)
        jmin = max(pt[1]-t,0)
        jmax = min(pt[1]+t,img.shape[1]-1)
        kmin = max(pt[2]-t,0)
        kmax = min(pt[2]+t,img.shape[2]-1)
        
        if img[pt] >= img[imin:imax+1, jmin:jmax+1, kmin:kmax+1].mean():
            seg[pt] = True
            needs_check += get_nbhd(pt,checked,img.shape)
        
        return seg
