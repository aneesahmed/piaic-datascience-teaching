import numpy as np
import matplotlib.pylab as plt

def plti(im, h=8, **kwargs):
    """
    Helper function to plot an image.
    """
    y = im.shape[0]
    x = im.shape[1]
    w = (y/x) * h
    plt.figure(figsize=(w,h))
    plt.imshow(im, interpolation="none", **kwargs)
    plt.axis('off')
    #input('press <ENTER> to continue')


#%matplotlib inline
im = plt.imread("airplane.png")
#plti(im)
im = im[400:3800,:2000,:]    
plti(im)
print( im.shape )
