import Asymmetry as A
import BorderIrregularity as B
import ColourVariation as C
import DifferentialStructures as D

def getFeatures(filename):
    
    features = []
    
    features.extend(A.calculateFeatures)
    features.extend(B.calculateFeatures)
    features.extend(C.calculateFeatures)
    features.extend(D.calculateFeatures)
    
    return features

if __name__ == "__main__":
    import sys
    getFeatures(sys.argv[1])
