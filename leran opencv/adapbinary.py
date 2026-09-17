import cv2
import numpy as np


#  自适应阈值

img = cv2.imread("d:\\shenfen\\math.jpg")
img1 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
dst = cv2.adaptiveThreshold(img1,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,0)#加inv就是翻转 
dst_2 = cv2.medianBlur(dst,5)
cv2.imshow('img',img)
cv2.imshow('dst',dst)
cv2.imshow('dst2',dst_2)
cv2.waitKey(0)