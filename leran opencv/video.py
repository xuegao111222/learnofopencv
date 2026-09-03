import cv2

# 创建窗口
cv2.namedWindow('video', cv2.WINDOW_NORMAL)
cv2.resizeWindow('video', 1080, 780)

# 获取视频设备或读取视频文件
cap = cv2.VideoCapture(0)
# cap = cv2.VideoCapture('D:\\wechat\\xwechat_files\\wxid_okacul1eyxqc22_6d92\\msg\\video\\2026-08\\14df81a8bb7ca80cb35f78feb06a5395_raw.mp4')
if not cap.isOpened():
    print("摄像头打开失败，检查编号或是否被占用")
    exit()

# 先读一帧并做旋转，再按旋转后的真实尺寸创建 VideoWriter
ret, frame = cap.read()
if not ret:
    print("读取第一帧失败")
    cap.release()
    exit()

##frame = cv2.rotate(frame, cv2.ROTATE_90_CLOCKWISE)  # 再顺时针转 90°

h, w = frame.shape[:2]  # shape 是 (高, 宽)
fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # .mp4 用 mp4v，不要用 MJPG
vw = cv2.VideoWriter("D:\\shenfen\\hha.mp4", fourcc, 25, (w, h))
if not vw.isOpened():
    print("VideoWriter 打开失败，检查目录 D:\\shenfen 是否存在")
    cap.release()
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        print("读取失败")
        break

   ##frame = cv2.rotate(frame, cv2.ROTATE_90_CLOCKWISE)  # 再顺时针转 90°
    cv2.imshow('video', frame)

    # 写数据到多媒体文件
    vw.write(frame)

    key = cv2.waitKey(10)
    if key & 0xFF == ord('q'):
        break

cap.release()
vw.release()
cv2.destroyAllWindows()
