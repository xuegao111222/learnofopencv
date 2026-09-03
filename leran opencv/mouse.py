import cv2
import numpy as np
#鼠标回调函数
def mouse_callback(event,x,y,flags,userdata):
    print(event,x,y,flags,userdata)

#mouse_callback(1,100,100,16,"666")
cv2.namedWindow('mouse',cv2.WINDOW_NORMAL)
cv2.resizeWindow('mouse',640,360)

#设置鼠标回调
cv2.setMouseCallback('mouse',mouse_callback,"123")
img = np.zeros((360,640,3),np.uint8)
while True:

    cv2.imshow('mouse',img)
    key = cv2.waitKey()
    if(key & 0xFF == ord('q')):
        break
cv2.destroyAllWindows()