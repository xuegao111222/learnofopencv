import cv2
import numpy as np

img = cv2.imread("d:\\shenfen\\math.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 1. 二值化：白底黑字（注意：THRESH_BINARY，不要INV！）
binary = cv2.adaptiveThreshold(gray, 255, 
    cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 15, 10)

# 此时 binary 是：白纸（255）+ 黑字/黑线（0）

# 2. 统计每一行的黑色像素个数
black_count = np.sum(binary == 0, axis=1)  # 每行有多少个黑像素

# 3. 找到黑色特别多的行（就是横线所在的行），直接涂白
threshold = np.max(black_count) * 0.5  # 黑色像素超过最大值一半的，判定为横线
for y in range(binary.shape[0]):
    if black_count[y] > threshold:
        binary[y, :] = 255  # 整行涂白，横线消失

kernel = np.ones((5,5),np.uint8)
dst_3 = cv2.erode(binary,kernel,iterations=1)
cv2.imshow('original', img)
cv2.imshow('clean', binary)
cv2.imshow('dst_3',dst_3)
cv2.waitKey(0)