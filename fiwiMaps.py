from saliency_map import SaliencyMap
from utils import *
from os import listdir
from os.path import isfile, join
import numpy as np

onlyfiles = [f for f in sorted(listdir('stimuli')) if isfile(join('stimuli', f))]
oi = OpencvIo()
u = Util()

## option 1: using saliency_map.py
for f in onlyfiles:
    maps = 0
    print('Doing saliency map of file {}'.format(f))
    src = oi.imread('stimuli/'+f)
    sm = SaliencyMap(src)
    # np.savetxt('results/'+f+'.txt',sm.map)
    cv.imwrite( 'results/sm'+f, np.uint8(u.normalize_range(sm.map)))
    cv.imwrite( 'results/cmcolor'+f, np.uint8(u.normalize_range(sm.cm.maps['color'])))
    cv.imwrite( 'results/cmintensity'+f, np.uint8(u.normalize_range(sm.cm.maps['intensity'])))
    cv.imwrite( 'results/cmorientation'+f, np.uint8(u.normalize_range(sm.cm.maps['orientation'])))
    maps+=4
    for i in sm.fm.maps['intensity']:
        maps+=1
        cv.imwrite( 'results/fmintensity'+ str(maps) + f, np.uint8(u.normalize_range(i.astype('float64'))))
    for i in sm.fm.maps['colors']['bg']:
        maps+=1
        cv.imwrite( 'results/fmcolorsbg'+ str(maps) + f, np.uint8(u.normalize_range(i.astype('float64'))))
    for i in sm.fm.maps['colors']['ry']:
        maps+=1
        cv.imwrite( 'results/fmcolorsry'+ str(maps) + f, np.uint8(u.normalize_range(i.astype('float64'))))
    for i in sm.fm.maps['orientations']['0']:
        maps+=1
        cv.imwrite( 'results/fmorientations0'+ str(maps) + f, np.uint8(u.normalize_range(i.astype('float64'))))
    for i in sm.fm.maps['orientations']['45']:
        maps+=1
        cv.imwrite( 'results/fmorientations45'+ str(maps) + f, np.uint8(u.normalize_range(i.astype('float64'))))
    for i in sm.fm.maps['orientations']['90']:
        maps+=1
        cv.imwrite( 'results/fmorientations90'+ str(maps) + f, np.uint8(u.normalize_range(i.astype('float64'))))
    for i in sm.fm.maps['orientations']['135']:
        maps+=1
        cv.imwrite( 'results/fmorientations135'+ str(maps) + f, np.uint8(u.normalize_range(i.astype('float64'))))
    for i in sm.gp.maps['intensity']:
        maps+=1
        cv.imwrite( 'results/gpintensity'+ str(maps) + f, np.uint8(u.normalize_range(i.astype('float64'))))
    for i in sm.gp.maps['colors']['b']:
        maps+=1
        cv.imwrite( 'results/gpcolorsb'+ str(maps) + f, np.uint8(u.normalize_range(i.astype('float64'))))
    for i in sm.gp.maps['colors']['g']:
        maps+=1
        cv.imwrite( 'results/gpcolorsg'+ str(maps) + f, np.uint8(u.normalize_range(i.astype('float64'))))
    for i in sm.gp.maps['colors']['y']:
        maps+=1
        cv.imwrite( 'results/gpcolorsy'+ str(maps) + f, np.uint8(u.normalize_range(i.astype('float64'))))
    for i in sm.gp.maps['colors']['r']:
        maps+=1
        cv.imwrite( 'results/gpcolorsr'+ str(maps) + f, np.uint8(u.normalize_range(i.astype('float64'))))
    for i in sm.gp.maps['orientations']['0']:
        maps+=1
        cv.imwrite( 'results/gporientations0'+ str(maps) + f, np.uint8(u.normalize_range(i.astype('float64'))))
    for i in sm.gp.maps['orientations']['45']:
        maps+=1
        cv.imwrite( 'results/gporientations45'+ str(maps) + f, np.uint8(u.normalize_range(i.astype('float64'))))
    for i in sm.gp.maps['orientations']['90']:
        maps+=1
        cv.imwrite( 'results/gporientations90'+ str(maps) + f, np.uint8(u.normalize_range(i.astype('float64'))))
    for i in sm.gp.maps['orientations']['135']:
        maps+=1
        cv.imwrite( 'results/gporientations135'+ str(maps) + f, np.uint8(u.normalize_range(i.astype('float64'))))

    print('Saliency map of file {} ready with {} maps'.format(f, maps))
    break