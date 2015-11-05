import Asymmetry as A
import BorderIrregularity as B
import ColourVariation as C
import DifferentialStructures as D
import numpy as np

def getFeatures(filename):
    
    features = []
    
    features.extend(A.calculateFeatures(filename))
    features.extend(B.calculateFeatures(filename))
    features.extend(C.calculateFeatures(filename))
    features.extend(D.calculateFeatures(filename))
    
    #print features
    return features

if __name__ == "__main__":
    import sys
    getFeatures(sys.argv[1])
