import cv2

#创建窗口
cv2.namedWindow('video',cv2.WINDOW_NORMAL)
cv2.resizeWindow('video',780,480)
#获取视频设备或读取视频文件
cap = cv2.VideoCapture(1)
#cap = cv2.VideoCapture('D:\\wechat\\xwechat_files\\wxid_okacul1eyxqc22_6d92\\msg\\video\\2026-08\\14df81a8bb7ca80cb35f78feb06a5395_raw.mp4')
while True:
    ret,frame = cap.read()

    cv2.imshow('video',frame)

    key = cv2.waitKey(10)
    if(key & 0xFF == ord('q')):
        break

cap.release()
cv2.destroyAllWindows()