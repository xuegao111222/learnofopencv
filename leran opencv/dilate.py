import cv2
import numpy as np



img = cv2.imread("d:\\shenfen\\test1.png")
#img1= cv2.imread("d:\\shenfen\\test2.png")
# img1 = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
kernel = cv2.getStructuringElement(cv2.MORPH_RECT,(7,7))
#卷积核越大  效果越明显


#这就是开运算的底层逻辑   先进行腐蚀再进行膨胀  这样可以有效处理黑底白字
#dst1 = cv2.erode(img,kernel,iterations=1)

#dst = cv2.dilate(dst1,kernel,iterations=1)
cv2.imshow('img',img)
# 开操作   MORPH_OPEN
#dst = cv2.morphologyEx(img,cv2.MORPH_OPEN,kernel)
#闭运算 用于清除内部的噪点
#dst1 = cv2.morphologyEx(img1,cv2.MORPH_CLOSE,kernel)

#梯度  原图-腐蚀  kernel越大 轮廓就越粗  
dst2 = cv2.morphologyEx(img,cv2.MORPH_GRADIENT,kernel)

#cv2.imshow('dst1',dst1)
#cv2.imshow('dst',dst)
##cv2.imshow('dst1',dst1)
cv2.imshow('dst2',dst2)
cv2.waitKey(0)