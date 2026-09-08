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
img_1 = cv2.subtract(img,img2)
cv2.imshow('img_1',img_1)
while True:

    key = cv2.waitKey(0)
    if key & 0xff == ord('q'):
        break
cv2.destroyAllWindows()
#  图像的乘法和除法 multiply(A,B)  和  divide(A,B)   亮的更多或者变得更暗