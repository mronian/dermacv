import numpy as np
import cv2
import math

def calcB(img, x, y, angle):
    
    B1=B2=0
    
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            val = j-angle*(i-x)-y
            if val>0:
                B1=B1+1
            else :
                B2=B2+1
    
    return B1, B2

def calculateFeatures(filename):
    
    filename=filename+'_contour.png'
    original=cv2.imread(filename, cv2.IMREAD_UNCHANGED)
    
    ret,thresh = cv2.threshold(original,127,255,0)
    contours,hierarchy = cv2.findContours(thresh, 1, 2)
    
    features=[]
    
    cnt = contours[0]
    area=cv2.contourArea(cnt)
    convex_hull=cv2.convexHull(cnt)
    hull_area=cv2.contourArea(convex_hull)
    x,y,w,h = cv2.boundingRect(cnt)
    rect_area = w*h
    perimeter = cv2.arcLength(cnt,True)
    (x,y),(L1,L2),angle = cv2.fitEllipse(cnt)
    
    
    B11, B12=calcB(original, x, y, angle)
    B21, B22=calcB(original, x, y, 180-angle)
    
    
    f1_solidity=float(area)/hull_area
    f2_extent = float(area)/rect_area
    f3_equi_diameter = float(4*area)/(L1*np.pi)
    f4_circularity=float(4*area*np.pi)/(perimeter*L1)
    f5_ratio_axis=float(L1)/L2
    f6_ratio_boundingbox=float(w)/h
    f7_ratio_periarea=float(perimeter)/area
    f8_ratio_L1=float(B11-B12)/area
    f9_ratio_L2=float(B21-B22)/area
    f10_ratio_areasL1=float(B11)/B21
    f11_ratios_areasL2=float(B21)/B22
    
    features.append(f1_solidity)
    features.append(f2_extent)
    features.append(f3_equi_diameter)
    features.append(f4_circularity)
    features.append(f5_ratio_axis)
    features.append(f6_ratio_boundingbox)
    features.append(f7_ratio_periarea)
    features.append(f8_ratio_L1)
    features.append(f9_ratio_L2)
    features.append(f10_ratio_areasL1)
    features.append(f11_ratios_areasL2)
    
    return features

if __name__ == "__main__":
    import sys
    calculateFeatures(sys.argv[1])
