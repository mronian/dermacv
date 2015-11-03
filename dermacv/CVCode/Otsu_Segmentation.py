import numpy as np
import cv2
import math
import otsu

def segment(filename):
    
    original=cv2.imread(filename, cv2.IMREAD_UNCHANGED)
    grayscale=cv2.cvtColor(original, cv2.COLOR_BGR2GRAY)
    
    #print thresh.shape
    get_otsu=otsu.otsu(grayscale)
    cv2.imshow('Original', get_otsu)
    
    cv2.waitKey()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    import sys
    segment(sys.argv[1])
