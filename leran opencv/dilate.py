import cv2
import numpy as np



img = cv2.imread("d:\\shenfen\\test2.png")
#img1= cv2.imread("d:\\shenfen\\test2.png")
# img1 = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
kernel = cv2.getStructuringElement(cv2.MORPH_RECT,(19,19))
#卷积核越大  效果越明显


#这就是开运算的底层逻辑   先进行腐蚀再进行膨胀  这样可以有效处理黑底白字
#dst1 = cv2.erode(img,kernel,iterations=1)

#dst = cv2.dilate(dst1,kernel,iterations=1)
cv2.imshow('img',img)
# 开操作   MORPH_OPEN
#dst = cv2.morphologyEx(img,cv2.MORPH_OPEN,kernel)
#闭运算 用于清除内部的噪点
#dst1 = cv2.morphologyEx(img1,cv2.MORPH_CLOSE,kernel)

#梯度  原图-腐蚀  kernel越大 轮廓就越粗  核心用途：提取图像中比背景更亮的细节部分。
'''具体来说，顶帽运算适用于以下场景：
提取亮细节（高光/亮斑）
开运算会去除比结构元素小的亮区域，顶帽运算把这些被去除的亮细节"抠"出来。
例如：从不均匀光照的背景中提取明亮的文字、斑点、划痕等。
背景校正后的细节增强
当图像背景不均匀（如光照渐变、阴影）时，直接用阈值分割效果很差。
先用顶帽运算去除缓慢变化的背景，再对结果做阈值处理，能显著提升分割效果。
文本/文档图像增强
在文档扫描图像中，顶帽运算可以去除背景噪声，突出文字笔画，便于后续 OCR 识别。
缺陷检测
在工业质检中，用于提取材料表面的亮点缺陷（如划痕、裂纹处的反光）。'''
#dst2 = cv2.morphologyEx(img,cv2.MORPH_GRADIENT,kernel)


#顶帽运算  原始图像-开运算
dst2 = cv2.morphologyEx(img,cv2.MORPH_TOPHAT,kernel)
#黑帽运算  原图 - 闭运算  求大的区域里小的噪点  就是将噪点取出来
dst3 = cv2.morphologyEx(img,cv2.MORPH_BLACKHAT,kernel)
#cv2.imshow('dst1',dst1)
#cv2.imshow('dst',dst)
##cv2.imshow('dst1',dst1)
cv2.imshow('dst2',dst3)
cv2.waitKey(0)