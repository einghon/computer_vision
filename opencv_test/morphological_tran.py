#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 23 14:09:03 2019

@author: nyeinchan
"""

import cv2
import numpy as np
img = cv2.imread('opening.png',0)
kernel = np.ones((5,5),np.uint8)

cv2.imshow("original",img)

'''
erosion = cv2.erode(img,kernel,iterations = 1)
dilation = cv2.dilate(img,kernel,iterations = 1)
'''

opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)

cv2.imshow('res',opening)
#cv2.imshow('dilate',dilation)

cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.waitKey(1)