import cv2
import numpy as np


#  全局二值化

img = cv2.imread("d:\\shenfen\\math.jpg")
img1 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret,dst = cv2.threshold(img1,90,220,cv2.THRESH_BINARY)#加inv就是翻转 
cv2.imshow('img',img)
cv2.imshow('dst',dst)
cv2.waitKey(0)