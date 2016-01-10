import sys
from saliency_map import SaliencyMap
from utils import OpencvIo

oi = OpencvIo()
src = oi.imread("stimuli/agoda.png")
sm = SaliencyMap(src)
oi.imshow_array([sm.map])
