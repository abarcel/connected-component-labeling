import numpy as np

class TSCCL(): #Two-Step Connected Component Labeling
    def __init__(self, img, Nsize=4):    
        self.label = 0
        self.SL = np.array([]) #SL = Swap Label
        
        pad_img = np.zeros([img.shape[0]+2, img.shape[1]+2])
        pad_img[1:img.shape[0]+1, 1:img.shape[1]+1] = np.where(img>0, -1, 0)
        self.LB = pad_img
        
        neighbor = np.vstack([(x, y) for x in range(-1, 2) for y in range(-1, 2)])
        if Nsize == 4:
            self.neighbor = neighbor[1:5:2]
        elif Nsize == 8:
            self.neighbor = neighbor[:4]
        
    def forward_find_component(self):
        for L in range(self.LB.shape[0]):
            for P in range(self.LB.shape[1]):
                if self.LB[L, P] == -1:
                    self.search(L, P, 1)
                    
    def backward_find_component(self):
        for L in reversed(range(self.LB.shape[0])):
            for P in reversed(range(self.LB.shape[1])):
                if self.LB[L, P] != 0:
                    self.search(L, P, -1)
                    
    def search(self, L, P, direction):
        NL = np.array([self.LB[L+NB[0]][P+NB[1]] for NB in direction*self.neighbor]) #NL = Neighbor Label
        
        if np.max(NL) > 0:    
            self.LB[L, P] = np.min(NL[NL > 0])
            if len(np.unique(NL[NL > 0])) > 1: 
                self.SL = np.concatenate((self.SL, np.unique(NL[NL > 0])))
                
        elif np.min(NL) == -1:
            self.label += 1
            self.LB[L, P] = self.label
            
    def label_swap(self):
        self.SL = self.SL.reshape((-1, 2))
        self.SL = self.SL[self.SL[:,1].argsort()]
        self.SL = self.SL[self.SL[:,0].argsort(kind='mergesort')]
        for i in reversed(range(len(self.SL))):
            self.LB[self.LB==self.SL[i][1]] = self.SL[i][0]
            
    def result(self):
        self.forward_find_component()
        self.backward_find_component()
        self.label_swap()
        return self.LB[1:self.LB.shape[0]-1, 1:self.LB.shape[1]-1].astype('uint8')

