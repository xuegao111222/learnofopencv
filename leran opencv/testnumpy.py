import numpy as np
import cv2
# a = np.array([1,2,3])
# print(a)

#定义zeros矩阵
# c = np.zeros((8,8),np.uint8)
# print(c)

img = np.zeros((480,640,3),np.uint8)
# count = 0
# while count < 200:
#     img[count,100,0] = 255
#     count = count + 1
# print(img[100,100])


roi = img[100:200,100:200]
roi[:,:] = [0,0,255] 

cv2.imshow('img',img)
key = cv2.waitKey(0)
if key & 0xFF == ord('q'):
    cv2.destroyAllWindows()

# d = np.ones((8,8),np.uint8)
# print(d)

#定义full矩阵
#e = np.full((8,8),255,np.uint8)
#print(e) 

#定义单位矩阵identity  斜对角是1其他是0  正斜对角
#f = np.identity(8)
#print(f)

# g = np.eye(5,3)
# print(g)