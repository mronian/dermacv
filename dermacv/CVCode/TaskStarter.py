import illumination_correction
import hist_eq
import gamma_correction
import Otsu_Segmentation
import getFeatures

def begin(filename):
    illumination_correction.illu_Correct(filename)
    Otsu_Segmentation.segment(filename)
    getFeatures.getFeatures(filename)

if __name__ == "__main__":
    import sys
    begin(sys.argv[1])
