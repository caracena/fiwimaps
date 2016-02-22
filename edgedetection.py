import cv2
import sys
from os import listdir
from os.path import isfile, join
import numpy as np

onlyfiles = [f for f in sorted(listdir('stimuli')) if isfile(join('stimuli', f))]

for f in onlyfiles:
    print('Doing edge detection of file {}'.format(f))
    # Read the image
    image = cv2.imread('stimuli/'+f)
    edges = cv2.Canny(image,100,200)
    np.savetxt('edges/'+f+'.txt',edges)
    print('Ready edge detection for file {}'.format(f))
