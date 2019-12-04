# -*- coding: utf-8 -*-
"""
Using Matt Hancock's ( notmatthancock.github.io ) neighborhood definition/
retrieval code, segments an image based on similarity of each voxel to its
immediate neighbors, i.e. if pt = [i,j,k], the neighbors are defined as
the triplet [(i +/- 1), (j +/- 1), (k +/- 1)] for a neighborhood size of 1.

All credit for this code belongs to Matt Hancock, from whom it was directly
adapted.
"""

import numpy as np

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
    