import io
import cv2 as cv
from utils import OpencvIo
import sys
from os import listdir
from os.path import isfile, join
import numpy as np

onlyfiles = [f for f in sorted(listdir('files')) if isfile(join('files', f))]

## use cv.pyDown to reduce matix
for f in onlyfiles:
    print('Reading file: {}'.format(f))
    fl = io.open("files/" + f)
    arr = np.zeros((1366,768))
    for line in fl.readlines():
        values = line.split(",")
        arr[int(float(values[2]))][int(float(values[3]))] += int(float(values[1]))
    arr = map(cv.pyrDown, [arr])
    np.savetxt('matrix/'+f+'.txt',arr[0])
    print('file {} ready'.format(f))
