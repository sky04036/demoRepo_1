# -*- coding: utf-8 -*-
"""
Created on Wed Oct  3 19:17:53 2018

@author: sky04
"""

import cv2

#調用攝像頭
cap = cv2.VideoCapture(0)
if(cap.isOpened()):
    print("webCam activated")
while(cv2.waitKey(3)!=ord('q')):
    ret,frame = cap.read()
    cv2.imshow("webCam",frame)
else:
    print("Failed to open Cam")
cap.released()
cv2.destroyAllWindows