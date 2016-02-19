import sys
from saliency_map import SaliencyMap
from utils import OpencvIo
from os import listdir
from os.path import isfile, join
import numpy as np

onlyfiles = [f for f in sorted(listdir('stimuli')) if isfile(join('stimuli', f))]
oi = OpencvIo()

## option 1: using saliency_map.py
for f in onlyfiles:
    print('Doing saliency map of file {}'.format(f))
    src = oi.imread('stimuli/'+f)
    sm = SaliencyMap(src)
    np.savetxt('results/'+f+'.txt',sm.map)
    print('Saliency map of file {} ready'.format(f))
