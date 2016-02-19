import cv2
import sys
from os import listdir
from os.path import isfile, join
import numpy as np

onlyfiles = [f for f in sorted(listdir('stimuli')) if isfile(join('stimuli', f))]

# Create the haar cascade
faceCascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

for f in onlyfiles:
    print('Doing face detection of file {}'.format(f))
    # Read the image
    image = cv2.imread('stimuli/'+f)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Detect faces in the image
    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
        flags = cv2.CASCADE_SCALE_IMAGE
    )
    np.savetxt('faces/'+f+'.txt',faces)
    print "Found {0} faces!".format(len(faces))
