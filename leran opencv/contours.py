import cv2
import numpy


def drawShape(src,points):
    i=0
    while i < len(points):
        if(i == len(points) - 1):
            x,y = points[i][0]
            x1,y1 = points[0][0]
            cv2.line(src,(x,y),(x1,y1),(0,0,255),1)
        else :
            x,y = points[i][0]
            x1,y1 = points[i+1][0]
            cv2.line(src,(x,y),(x1,y1),(0,0,255),1)
        i = i + 1
img = cv2.imread("d:\\shenfen\\hand2.png")
# print(img.shape)
# #转变为单通道
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
print(gray.shape)

#二值化
ret,binary = cv2.threshold(gray,150,255,cv2.THRESH_BINARY)
print(binary.shape)
 
#轮廓查找
contours, hierarchy = cv2.findContours(binary,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)


#绘制轮廓
cnt = contours[0]                                # 取第0个轮廓
e = 20                                           # 近似精度（epsilon）
approx = cv2.approxPolyDP(cnt, e, True)          # 多边形近似，结果赋给 approx
drawShape(img, approx)                           # 画近似多边形
# #轮廓面积
# area = cv2.contourArea(contours[0])
# print("area=%d"%(area))


# #计算周长
# len = cv2.arcLength(contours[0],False)  #第二个值代表是否闭合  
# print("len=%d"%len)

# print(contours)
cv2.imshow('img',img)
# cv2.imshow('binary',binary)
cv2.waitKey(0)