#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 23 09:45:48 2019

@author: nyeinchan
"""

import numpy as np
import cv2

img = cv2.imread('puppy.jpg',cv2.IMREAD_COLOR)

#cv2.line(img,(0,0),(150,300),(255,255,255),15)
#cv2.circle(img,(100,63), 55, (0,255,0), -1)
#pts = np.array([[10,5],[20,30],[70,20],[50,10]], np.int32)
# OpenCV documentation had this code, which reshapes the array to a 1 x 2. I did not 
# find this necessary, but you may:
#pts = pts.reshape((-1,1,2))
#cv2.polylines(img, [pts], True, (0,255,255), 3)

font = cv2.FONT_HERSHEY_SIMPLEX
#cv2.putText(img,'Ei Nghon is lit!',(200,100), font, 1, (100,255,155), 2, cv2.LINE_AA)

#rect = (161,79,150,150)
cv2.rectangle(img,(200,0),(590,380),(0,255,0),3)

#particular pixel
px = img[55,55]
img[55,55] = [255,255,255]
px = img[55,55]
print(px)

#region on an image
px = img[100:150,100:150]
print(px)

#img[100:150,100:150] = [255,255,255]
print(img.shape)
print(img.size)
print(img.dtype)

cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.waitKey(1)