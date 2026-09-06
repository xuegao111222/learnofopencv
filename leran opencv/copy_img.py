import cv2

import numpy as np


img = cv2.imread("D:\\shenfen\\123.png")
#浅拷贝
img2 = img
#深拷贝
img3 = img.copy()
img[10:100,10:100] = [0,0,255]
cv2.imshow('img',img)
cv2.imshow('img2',img2)
cv2.imshow('img3',img3)
cv2.waitKey(0)