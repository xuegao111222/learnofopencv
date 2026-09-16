import cv2
import numpy as np


img = cv2.imread("D:\\shenfen\\img1.png")
new = cv2.resize(img,(218,107))
new_2 = cv2.resize(img,(1294,642))
new_3 = cv2.flip(img,-1)# filpCode参数   ==0  上下翻转  大于零左右翻转  小于0  上下左右翻转
print(img.shape)
cv2.imshow('img',img)
cv2.imshow('new',new)
cv2.imshow('new_3',new_3)
cv2.waitKey(0)


