import cv2

img = cv2.imread('d:\\shenfenzheng.jpg')

cv2.namedWindow('img', cv2.WINDOW_NORMAL)
while True:
    cv2.imshow('img', img)

    key = cv2.waitKey(0)

    if (key & 0xFF == ord('q')):
        break
    elif (key & 0xFF == ord('s') ):
        cv2.imwrite("d:\\shenfen\\123.png",img)

cv2.destroyAllWindows()