import sys
from saliency_map import SaliencyMap
from utils import OpencvIo
from os import listdir
from os.path import isfile, join
import numpy as np

onlyfiles = [f for f in sorted(listdir('stimuli')) if isfile(join('stimuli', f))]

for f in onlyfiles:
        oi = OpencvIo()
        src = oi.imread("stimuli/"+f)
        sm = SaliencyMap(src)
        np.savetxt('results/'+f+'.txt',sm.map)
