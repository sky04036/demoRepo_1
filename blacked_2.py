# -*- coding: utf-8 -*-
"""
Created on Sat Sep 29 10:52:28 2018

@author: sky04
"""
import matplotlib.pyplot as plt 
import matplotlib.image as mpimg 
import numpy as np
import cv2

demo = mpimg.imread('717682.png') # load png
# load as an array
demo.shape #(512, 512, 3)

plt.imshow(demo) # show image in console
plt.axis('off') #get rid of axis
plt.show()

def blacked(rgb):
    return np.dot(rgb[...,:3], [0.05, 0.05, 0.05])#return image to black 
#show in console
image_new = blacked(demo)
plt.imshow(image_new, cmap='Greys_r')
plt.axis('off')
plt.show()
#show in window
cv2.namedWindow("Blacked", cv2.WINDOW_NORMAL);
cv2.resizeWindow("Blacked", 800, 600);
cv2.imshow("Blacked",image_new)
cv2.waitKey(0)
#cv2.destroyallwindows