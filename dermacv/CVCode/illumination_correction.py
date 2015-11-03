import numpy as np 
import cv2
#from django.conf import settings
import os
import math
import numpy as np
from sklearn.cross_validation import train_test_split
from sklearn import linear_model
from sklearn.metrics import mean_squared_error, accuracy_score
#from matplotlib import pyplot as plt

def illu_Correct(filename):
    #pathr=settings.BASE_DIR+'/media/uploads/'
    #filenamer=pathr+filename
    #filenamer="../"
    #print filenamer
    original=cv2.imread(filename, cv2.IMREAD_UNCHANGED)
    #cv2.namedWindow('Illumination Corrected Image')
    #cv2.namedWindow('Original')
    print "Correcting Illumination using Corner Points as Healthy Skin"
    
    hsv=cv2.cvtColor(original, cv2.COLOR_BGR2HSV)
    
    height=hsv.shape[0]
    width=hsv.shape[1]
    channels=hsv.shape[2]

    value=hsv[:,:,2]
    v_norm=value.astype(float)
    
    maxi=np.amax(value)
    mini=np.amin(value)    
    
    v_norm-=mini
    v_norm/=(maxi-mini)
    
    corrected_RGB=np.zeros((height, width, channels))
    
    pixel_set=[]
    features = []
    
    for i in range(20):
        for j in range(20):
            f=[]
            pixel_set.append(v_norm[i,j])
            f.append(i*i)
            f.append(j*j)
            f.append(i*j)
            f.append(i)
            f.append(j)
            f.append(1)
            features.append(f)
        
    for i in range(height-20,height):
        for j in range(20):
            f=[]
            pixel_set.append(v_norm[i,j])
            f.append(i*i)
            f.append(j*j)
            f.append(i*j)
            f.append(i)
            f.append(j)
            f.append(1)
            features.append(f)
        
    for i in range(20):
        for j in range(width-20, width):
            f=[]
            pixel_set.append(v_norm[i,j])
            f.append(i*i)
            f.append(j*j)
            f.append(i*j)
            f.append(i)
            f.append(j)
            f.append(1)
            features.append(f)
        
    for i in range(height-20, height):
        for j in range(width-20, width):
            f=[]
            pixel_set.append(v_norm[i,j])
            f.append(i*i)
            f.append(j*j)
            f.append(i*j)
            f.append(i)
            f.append(j)
            f.append(1)
            features.append(f)
    
    
    b=np.array(pixel_set)
    a=np.array(features)
    
    clf=linear_model.LinearRegression()

    clf.fit(a,b)

    c=clf.coef_

    for i in range(height):
        for j in range(width):
            f=[]
            f.append(i*i)
            f.append(j*j)
            f.append(i*j)
            f.append(i)
            f.append(j)
            f.append(1)
            z=clf.predict(f)
            
            v=v_norm[i,j]/z
            if v!=np.inf:
                v_norm.itemset((i,j), v)
    
    maxi=np.amax(v_norm)
    mini=np.amin(v_norm)
    
    v_norm-=mini
    v_norm/=(maxi-mini)
    v_norm*=255

    v_norm=v_norm.astype(np.uint8)
    #
    #hist=[0]*256
    #
    #for i in range(height):
    #    for j in range(width):
    #        hist[v_norm[i,j]]=hist[v_norm[i,j]]+1
    #
    #print hist
    
    #hist = cv2.calcHist([v_norm],[0],None,[256],[0,255])
    #plt.hist(gray_img.ravel(),256,[0,256])
    #plt.title('Histogram for gray scale picture')
    #plt.show()
    #print v_norm
    
    hsv[:,:,2]=v_norm
    
    
    corrected_RGB=cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)
    #cv2.imshow('Original', original)
    #cv2.imshow('Illumination Corrected Image', corrected_RGB)
    
    cv2.imwrite("Corrected_Illumination.jpg", corrected_RGB)
    

if __name__ == "__main__":
    import sys
    illu_Correct(sys.argv[1])