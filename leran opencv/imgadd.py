import cv2
import numpy as np

img = cv2.imread("D:\\shenfen\\1.png")

#图的加法运算就是矩阵的加法运算
#因此  加法运算的两张图必须是相等的
#print(img.shape)

img2 = np.ones((206,228,3),np.uint8) * 50

cv2.imshow('orig',img)

result = cv2.add(img,img2)

cv2.imshow('result',result)

cv2.waitKey(0)
