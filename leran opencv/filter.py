import cv2
import numpy as np

img = cv2.imread("d:\\shenfen\\jiege.jpg")

# kernel = np.ones((5,5),np.float32) / 25

# dst = cv2.filter2D(img,-1,kernel)

#dst = cv2.blur(img,(5,5)) 均值滤波

#dst = cv2.GaussianBlur(img,(5,5),sigmaX=1)#高斯滤波  主要解决高斯噪点
dst = cv2.bilateralFilter(img,7,1000,1000)
cv2.imshow("dst",dst)
cv2.imshow("img",img)
cv2.waitKey(0)