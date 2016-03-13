from utils import *
from os import listdir
from os.path import isfile, join


def make_gaussian_pyramid(src):
    # gaussian pyramid | 0 ~ 8(1/256) . not use 0 and 1.
    maps = {'intensity': [],
            'colors': {'b': [], 'g': [], 'r': []},
            'orientations': {'0': [], '45': [], '90': [], '135': []}}
    src = rgb2dklCart(src)
    b, g, r = cv.split(src)
    cs_index = ((0, 3), (0, 4), (1, 4), (1, 5), (2, 5), (2, 6))
    for i in xrange(0, 7):

        b, g, r = map(cv.pyrDown, [b, g, r])
        maps['colors']['b'].append(b)
        maps['colors']['g'].append(g)
        maps['colors']['r'].append(r)

        buf_its = np.zeros(b.shape)
        for y, x in itertools.product(xrange(len(b)), xrange(len(b[0]))):
            buf_its[y][x] = get_intensity(b[y][x], g[y][x], r[y][x])
        maps['intensity'].append(buf_its)
        for (orientation, index) in zip(sorted(maps['orientations'].keys()), xrange(4)):
            maps['orientations'][orientation].append(conv_gabor(buf_its, np.pi * index / 4))

    map1 = {}
    map1['intensity'] = []
    for c, s in cs_index:
        map1['intensity'].append(scale_diff(maps['intensity'][c], maps['intensity'][s]))

    maps['intensity'] = map1['intensity']
    return maps

def scale_diff(c, s):
    c_size = tuple(reversed(c.shape))
    return cv.absdiff(c, cv.resize(s, c_size, None, 0, 0, cv.INTER_NEAREST))

def get_intensity(b, g, r):
    return (np.float64(b) + np.float64(g) + np.float64(r)) / 3.

def get_colors(b, g, r, i, amax):
    b, g, r = map(lambda x: np.float64(x) if (x > 0.1 * amax) else 0., [b, g, r])
    nb, ng, nr = map(lambda x, y, z: max(x - (y + z) / 2., 0.), [b, g, r], [r, r, g], [g, b, b])
    ny = max(((r + g) / 2. - math.fabs(r - g) / 2. - b), 0.)

    if i != 0.0:
        return map(lambda x: x / np.float64(i), [nb, ng, nr, ny])
    else:
        return nb, ng, nr, ny

def conv_gabor(src, theta):
    kernel = cv.getGaborKernel((8, 8), 4, theta, 8, 1)
    return cv.filter2D(src, cv.CV_32F, kernel)

def rgb2dklCart(picture, conversionMatrix=None):
    """Convert an RGB image into Cartesian DKL space.
    """
    # Find the original dimensions of the picture
    origShape = picture.shape
    # this is the inversion of the dkl2rgb conversion matrix
    if conversionMatrix is None:
        conversionMatrix = np.asarray([
            # LUMIN->    %L-M->        L+M-S
            [0.25145542, 0.64933633, 0.09920825],
            [0.78737943, -0.55586618, -0.23151325],
            [0.26562825, 0.63933074, -0.90495899]])
    else:
        conversionMatrix = np.linalg.inv(conversionMatrix)
    # Reshape the picture so that it can multiplied by the conversion matrix
    red = picture[:, :, 0]
    green = picture[:, :, 1]
    blue = picture[:, :, 2]
    dkl = np.asarray([red.reshape([-1]),
                         green.reshape([-1]),
                         blue.reshape([-1])])
    # Multiply the picture by the conversion matrix
    dkl = np.dot(conversionMatrix, dkl)
    # Reshape the picture so that it's back to it's original shape
    dklPicture = np.reshape(np.transpose(dkl), origShape)
    return dklPicture

onlyfiles = [f for f in sorted(listdir('stimuli')) if isfile(join('stimuli', f))]
oi = OpencvIo()
u = Util()
for f in onlyfiles:
    print('Doing saliency map of file {}'.format(f))
    src = oi.imread('stimuli/'+f)
    sm = make_gaussian_pyramid(src)

    for i in xrange(0,len(sm['intensity'])):
        cv.imwrite( 'results/intensity'+str(i)+f, np.uint8(u.normalize_range(sm['intensity'][i])))
    for key in sm['colors']:
        for i in xrange(0,len(sm['colors'][key])):
            cv.imwrite( 'results/colors'+key+str(i)+f, np.uint8(u.normalize_range(sm['colors'][key][i])))
    for key in sm['orientations']:
        for i in xrange(0,len(sm['orientations'][key])):
            cv.imwrite( 'results/orientations'+key+str(i)+f, np.uint8(u.normalize_range(sm['orientations'][key][i])))
    break





