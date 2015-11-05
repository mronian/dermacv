import numpy as np
import cv2
import math

def euclidD(A, B):
    return math.sqrt(math.pow(A[0]-B[0],2)+math.pow(A[1]-B[1],2)+math.pow(A[2]-B[2],2))

def calculateFeatures(filename):
    
    mask_path=filename+'_contour.png'
    image_path=filename+'_orig.jpg'
    print image_path, mask_path
    
    original=cv2.imread(image_path, cv2.IMREAD_UNCHANGED)
    mask=cv2.imread(mask_path, cv2.IMREAD_UNCHANGED)
    features=[]
    mask2=mask.copy()
    contours,hierarchy = cv2.findContours(mask2, 1, 2)
    cnt = contours[0]
    area=cv2.contourArea(cnt)
    I1=[]
    I2=[]
    I3=[]
    features=[]
    counter=0
    White=0
    Black=0
    LightBrown=0
    Red=0
    DarkBrown=0
    BlueGray=0
    
    W=[1.0,1.0,1.0]
    B=[0.0,0.0,0.0]
    R=[0.2,0.2,0.8]
    LB=[0.0,0.4,0.6]
    DB=[0.0,0.0,0.2]
    BG=[0.6,0.6,0.2]
    
    original=original.astype(float)
    
    maxi=np.max(original)
    mini=np.min(original)
    original-=mini
    original/=(maxi-mini)
    #print mask
    for i in range (mask.shape[0]):
        for j in range (mask.shape[1]):
            if mask[i,j]==255:
                I1.append(original[i,j,0])
                I2.append(original[i,j,1])
                I3.append(original[i,j,2])
                dist_W=euclidD(W,original[i,j])
                dist_R=euclidD(R,original[i,j])
                dist_LB=euclidD(LB,original[i,j])
                dist_DB=euclidD(DB,original[i,j])
                dist_BG=euclidD(BG,original[i,j])
                dist_B=euclidD(B,original[i,j])
                mini=np.amin((dist_W, dist_B, dist_LB, dist_DB, dist_BG, dist_R))
                if mini==dist_W:
                    White=White+1
                elif mini==dist_R:
                    Red=Red+1
                elif mini==dist_LB:
                    LightBrown=LightBrown+1
                elif mini==dist_DB:
                    DarkBrown=DarkBrown+1
                elif mini==dist_BG:
                    BlueGray=BlueGray+1
                elif mini==dist_B:
                    Black=Black+1
    
    f24_max_all = np.max((I1,I2,I3))
    f25_min_all = np.min((I1,I2,I3))
    f26_mean_all = np.mean((I1,I2,I3))
    f27_var_all = np.var((I1,I2,I3))
    f28_max1=np.max(I1)
    f29_max2=np.max(I2)
    f30_max3=np.max(I3)
    f31_min1=np.min(I1)
    f32_min2=np.min(I2)
    f33_min3=np.min(I3)
    f34_mean1=np.mean(I1)
    f35_mean2=np.mean(I2)
    f36_mean3=np.mean(I3)
    f37_var1=np.var(I1)
    f38_var2=np.var(I2)
    f39_var3=np.var(I3)
    f40_ratio12=float(f34_mean1)/f35_mean2
    f41_ratio13=float(f34_mean1)/f36_mean3
    f42_ratio23=float(f35_mean2)/f36_mean3
    f43_W=float(White)/area
    f44_R=float(Red)/area
    f45_LB=float(LightBrown)/area
    f46_DB=float(DarkBrown)/area
    f47_BG=float(BlueGray)/area
    f48_B=float(Black)/area
    
    features.append(f24_max_all)
    features.append(f25_min_all)
    features.append(f26_mean_all)
    features.append(f27_var_all)
    features.append(f28_max1)
    features.append(f29_max2)
    features.append(f30_max3)
    features.append(f31_min1)
    features.append(f32_min2)
    features.append(f33_min3)
    features.append(f34_mean1)
    features.append(f35_mean2)
    features.append(f36_mean3)
    features.append(f37_var1)
    features.append(f38_var2)
    features.append(f39_var3)
    features.append(f40_ratio12)
    features.append(f41_ratio13)
    features.append(f42_ratio23)
    features.append(f43_W)
    features.append(f44_R)
    features.append(f45_LB)
    features.append(f46_DB)
    features.append(f47_BG)
    features.append(f48_B)
    
    return features

if __name__ == "__main__":
    import sys
    calculateFeatures(sys.argv[1])
