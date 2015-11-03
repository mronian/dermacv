import cv2
import os, sys
import numpy as np

def histogram(image):
  grayscale_array = []
  for h in range(image.shape[0]):
    for w in range(image.shape[1]):
      intensity = image[h,w]
      grayscale_array.append(intensity)

  total_pixels = image.size
  bins = range(0,257)
  img_histogram = np.histogram(grayscale_array, bins)
  return img_histogram


def otsu(image):
  hist = histogram(image)
  total = image.size
  current_max, t = 0, 0
  sumT, sumF, sumB = 0, 0, 0
  for i in range(0,256):
    sumT += i * hist[0][i]
  weightB, weightF = 0, 0
  varBetween, meanB, meanF = 0, 0, 0
  for i in range(0,256):
    weightB += hist[0][i]
    weightF = total - weightB
    if weightF == 0:
      break
    sumB += i*hist[0][i]
    sumF = sumT - sumB
    meanB = sumB/weightB
    meanF = sumF/weightF
    varBetween = weightB * weightF
    varBetween *= (meanB-meanF)*(meanB-meanF)
    if varBetween > current_max:
      current_max = varBetween
      t = i 
  print "threshold is:", t
  ret , binary=cv2.threshold(image, t, 255, cv2.THRESH_BINARY)
  return binary