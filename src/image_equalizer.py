#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np

def eq(img):
    cdf = np.cumsum(np.histogram(img.flatten(), range=[0, 256], bins=256)[0])
    mask = np.nonzero(cdf)
    min_ = np.min(cdf[mask])
    max_ = np.max(cdf[mask])
    cdf[mask] = cdf[mask] - min_
    eq = np.round((cdf * 255) / (max_ - min_))
    return eq[img].astype('uint8')

