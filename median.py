import sys
import numpy as np
from PIL import Image


def addpadding(src, pad):
    imarr = np.array(src)
    padimarr = np.zeros((imarr.shape[0]+2*pad, imarr.shape[1]+2*pad), dtype=np.uint8)
    padimarr[pad:padimarr.shape[0]-pad, pad:padimarr.shape[1]-pad] = imarr
    return padimarr


def removepadding(src, pad):
    imarr = np.array(src)
    result = imarr[pad:imarr.shape[0] - pad, pad:imarr.shape[1] - pad]
    return result


def medianfilter(src):
    target = addpadding(src, 1)
    for y in range(src.size[0]):
        for i in range(src.size[1]):
            local = target[i:i+3, y:y+3]
            target[i+1, y+1] = np.median(local)
    target = removepadding(target, 1)
    return target
    

source = Image.open(sys.argv[1])
size1 = source.size[0]
size2 = source.size[1]
target = medianfilter(source)
target = np.asarray(target, dtype=np.uint8)
Image.fromarray(target, 'L').save('median.png', 'PNG')
