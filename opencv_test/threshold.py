#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 23 10:30:03 2019

@author: nyeinchan
"""
import cv2
import numpy as np

#adaptive threshold
grayscaled = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

th = cv2.adaptiveThreshold(grayscaled, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 115, 1)

"""
#grayscaled and threshold
retval, threshold = cv2.threshold(grayscaled, 10, 255, cv2.THRESH_BINARY)
"""

cv2.imshow('original',img)
cv2.imshow('adaptive threshold',th)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.waitKey(1)