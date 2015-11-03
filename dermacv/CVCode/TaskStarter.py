import illumination_correction
import hist_eq
import gamma_correction
import Lesion_Segmentation

def begin(filename):
    illumination_correction.illu_Correct(filename)
    #Otsu_Segmentation.segment(filename)
    

if __name__ == "__main__":
    import sys
    begin(sys.argv[1])
