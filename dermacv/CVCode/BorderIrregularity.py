import numpy as np
import cv2
import math

def calculateFeatures(filename):
    
    mask_path=filename+'_contour.png'
    image_path=filename+'_orig.jpg'
    
    original=cv2.imread(image_path, cv2.IMREAD_UNCHANGED)
    mask=cv2.imread(mask_path, cv2.IMREAD_UNCHANGED)
    mask2=mask.copy()
    contours,hierarchy = cv2.findContours(mask2, 1, 2)
    features=[]
    
    cnt = contours[0]
    x,y,w,h = cv2.boundingRect(cnt)
    x=x+w/2
    y=y+h/2
    #print mask.shape
    kernel = np.ones((5,5),np.uint8)
    #ret,thresh = cv2.threshold(mask,127,255,0)
    gradient = cv2.morphologyEx(mask, cv2.MORPH_GRADIENT, kernel)
    #
    I1=[]
    I2=[]
    I3=[]
    features=[]
    P1=[[0,0,0]]
    P2=[[0,0,0]]
    P3=[[0,0,0]]
    P4=[[0,0,0]]
    counter=0
    original=original.astype(float)
    
    maxi=np.max(original)
    mini=np.min(original)
    original-=mini
    original/=(maxi-mini)
    #print mask
    for i in range (mask.shape[0]):
        for j in range (mask.shape[1]):
            if gradient[i,j]==255:
                I1.append(original[i,j,0])
                I2.append(original[i,j,1])
                I3.append(original[i,j,2])
                if i>x and j>y :
                    P1.append(original[i,j])
                elif i>x and j<y :
                    P2.append(original[i,j])
                elif i<x and j>y :
                    P3.append(original[i,j])
                elif i<x and j<y :
                    P4.append(original[i,j])
    P1AVG=np.average(P1, axis=0)
    P2AVG=np.average(P2, axis=0)
    P3AVG=np.average(P3, axis=0)
    P4AVG=np.average(P4, axis=0)
                    
    f12_avg1=np.average(I1)
    f13_avg2=np.average(I2)
    f14_avg3=np.average(I3)
    f15_var1=np.var(I1)
    f16_var2=np.var(I2)
    f17_var3=np.var(I3)
    f18=float(P1AVG[0]+P2AVG[0]+P3AVG[0])/3
    f19=float(P1AVG[1]+P2AVG[1]+P3AVG[1])/3
    f20=float(P1AVG[2]+P2AVG[2]+P3AVG[2])/3
    f21=np.var((P1AVG[0],P2AVG[0],P3AVG[0]))
    f22=np.var((P1AVG[1],P2AVG[1],P3AVG[1]))
    f23=np.var((P1AVG[2],P2AVG[2],P3AVG[2]))
    
    features.append(f12_avg1)
    features.append(f13_avg2)
    features.append(f14_avg3)
    features.append(f15_var1)
    features.append(f16_var2)
    features.append(f17_var3)
    features.append(f18)
    features.append(f19)
    features.append(f20)
    features.append(f21)
    features.append(f22)
    features.append(f23)
    
    return features

if __name__ == "__main__":
    import sys
    calculateFeatures(sys.argv[1])
