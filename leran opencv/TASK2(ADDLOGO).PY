"""
1.引入一张图片
2.引入一个logo  需要自己创建
3.水印的添加   （计算在什么地方添加   要在对应的地方扣掉）
4.利用add将图片叠加到一起

"""




import cv2
import numpy as np

def mouse_callback(event,x,y,flags,userdata):
    print(event,x,y,flags,userdata)



img1 = cv2.imread("d:\\shenfen\\img1.png")
print(img1.shape)
logo = np.zeros((321,647,3),np.uint8)

cv2.imshow('logo',logo)
cv2.setMouseCallback('logo',mouse_callback,"1")
# 替代你的 for 循环，瞬间完成“扣掉”操作
img1[247:292:22, 584:615] = (0, 0, 0) 
img1[247:292,599:599] = (0,0,0)
# 替代你的 for 循环，瞬间完成“扣掉”操作
logo[247:292:22, 584:615] = (102, 255, 0) 
logo[247:292,599:599] = (102,255,0)
result = cv2.add(img1,logo)
cv2.imshow('result',result)
cv2.waitKey(0)