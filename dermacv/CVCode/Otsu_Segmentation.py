import numpy as np
import cv2
import math
import otsu

def segment(filename):
    
    original=cv2.imread(filename, cv2.IMREAD_UNCHANGED)
    
    kernel = np.ones((5,5),np.uint8)
    height=original.shape[0]
    width=original.shape[1]
    
    grayscale=cv2.cvtColor(original, cv2.COLOR_BGR2GRAY)
    for i in range(height-120, height-6):
        for j in range(width-120, width-6):
            avg_val=0
            for k in range(i-2, i+3):
                for l in range(j-2, j+3):
                    avg_val=avg_val+grayscale[k,l]
            avg_val=avg_val/25
            grayscale.itemset((i,j), avg_val)
    
    #print thresh.shape
    get_otsu=otsu.otsu(grayscale)
    kernel = np.ones((5,5),np.uint8)
    dilation = cv2.erode(get_otsu,kernel,iterations = 3)
    dilation = cv2.dilate(dilation,kernel,iterations = 3)
    gradient = cv2.morphologyEx(dilation, cv2.MORPH_GRADIENT, kernel)
    cv2.imshow('Original2', grayscale)
    cv2.imshow('Original', gradient)
    cv2.imwrite('Otsu.jpg', dilation)
    cv2.waitKey()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    import sys
    segment(sys.argv[1])
