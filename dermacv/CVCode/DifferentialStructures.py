import numpy as np
import cv2
import math

def calculateFeatures(filename):
    
    original=cv2.imread(filename, cv2.IMREAD_UNCHANGED)
    img=cv2.cvtColor(original, cv2.COLOR_BGR2GRAY)
    energy=0
    contrast=0
    homogenity=0
    IDM=0
    entropy=0
    mean1=0
    row=img.shape[0]
    col=img.shape[1];
    gl=np.zeros((256,256))
    features=[]
    
    for i in range(row-1):
        for j in range(col-1):
            gl[img[i,j], img[i,j+1]]=gl[img[i,j], img[i,j+1]]+1
    
    gl=gl+gl.T            
    gl=gl/np.sum(gl, axis=0)
    
    
    for i in range(256):
        for j in range(256):
            energy=energy+gl[i,j]*gl[i,j]
            contrast=contrast+(i-j)*(i-j)*gl[i,j]
            homogenity=homogenity+float(gl[i,j])/(1+math.fabs(i-j))
            if i!=j:
                IDM=IDM+float(gl[i,j])/((i-j)*(i-j))
            if gl[i,j]!=0:
                entropy=entropy-gl[i,j]*math.log10(gl[i,j])
            mean1=mean1+0.5*(i*gl[i,j]+j*gl[i,j]);
    
    features.append(energy)
    features.append(contrast)
    features.append(homogenity)
    features.append(IDM)
    features.append(entropy)
    features.append(mean1)
    
    return features

if __name__ == "__main__":
    import sys
    calculateFeatures(sys.argv[1])
