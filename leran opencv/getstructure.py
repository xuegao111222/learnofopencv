import cv2
import numpy as np

#卷积核的类型  
#
img = cv2.imread("d:\\shenfen\\ruyuan.png")
kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(5,5))
print(kernel)
dst = cv2.erode(img,kernel,iterations=1)
cv2.imshow('img',img)
cv2.imshow('dst',dst)
cv2.waitKey(0)