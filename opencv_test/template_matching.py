#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 23 14:56:02 2019

@author: nyeinchan
"""

import cv2
import numpy as np

img_rgb = cv2.imread('main_img.jpg')
img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)

template = cv2.imread('match.jpg',0)
w, h = template.shape[::-1]

#We load the template and note the dimensions.
res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)
threshold = 0.7
loc = np.where( res >= threshold)

#mark all matches on the original image, using the coordinates we found in the gray image:
for pt in zip(*loc[::-1]):
    cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0,255,255), 2)


cv2.imshow('Detected',img_rgb)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.waitKey(1)