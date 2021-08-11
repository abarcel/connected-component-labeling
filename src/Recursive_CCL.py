#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np

class RCCL(): #Recursive Connected Component Labeling
    def __init__(self, img, Nsize=4):    
        self.label = 0
        
        pad_img = np.zeros([img.shape[0]+2, img.shape[1]+2])
        pad_img[1:img.shape[0]+1, 1:img.shape[1]+1] = np.where(img>0, -1, 0)
        self.LB = pad_img
        
        neighbor = np.vstack([(x, y) for x in range(-1, 2) for y in range(-1, 2)])
        if Nsize == 4:
            self.neighbor = neighbor[1::2] 
        elif Nsize == 8:
            self.neighbor = np.delete(neighbor, 4, axis=0)      
        
    def find_component(self):
        for L in range(self.LB.shape[0]):
            for P in range(self.LB.shape[1]):
                if self.LB[L, P] == -1:
                    self.label += 1
                    self.search(L, P)
                    
    def search(self, L, P):
        self.LB[L, P] = self.label
        for NB in self.neighbor:
            if self.LB[L+NB[0], P+NB[1]] == -1:
                self.search(L+NB[0], P+NB[1])
    
    def result(self):
        self.find_component()   
        return self.LB[1:self.LB.shape[0]-1, 1:self.LB.shape[1]-1].astype('uint8')

