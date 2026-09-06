import cv2
import numpy as np

img = cv2.imread('d:\\shenfen\\shenfenzheng.jpg')

print(img.shape)

#占用空间  高度*长度*通道数
print(img.size)


print(img.dtype)