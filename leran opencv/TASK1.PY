import cv2
import numpy as np

start_pos = None
mode = None            # None 或 'line' 或 'circle'，一个变量搞定

def mouse_callback(event, x, y, flags, userdata):
    global start_pos
    if mode is None or event != cv2.EVENT_LBUTTONDOWN:
        return

    if start_pos is None:          # 第一次点：都只是存起点
        start_pos = (x, y)
        return

    if mode == 'line':             # 第二次点：按模式画
        cv2.line(img, start_pos, (x, y), (0, 0, 255), 2)
        print("划线:", start_pos, "->", (x, y))
    elif mode == 'circle':
        radius = int(np.sqrt((x - start_pos[0])**2 + (y - start_pos[1])**2))
        cv2.circle(img, start_pos, radius, (255, 255, 0), 2)
        print("画圆: 圆心", start_pos, "半径", radius)
    start_pos = None               # 画完统一重置

cv2.namedWindow('img', cv2.WINDOW_NORMAL)
cv2.setMouseCallback('img', mouse_callback)
img = np.zeros((480, 640, 3), np.uint8)

while True:
    cv2.imshow('img', img)
    key = cv2.waitKey(10)

    if key & 0xFF == ord('l'):
        mode = 'line'
        print("划线模式")
    elif key & 0xFF == ord('c'):
        mode = 'circle'
        print("画圆模式")
    elif key & 0xFF == ord('x'):   # 按 x 关闭，回到"点了没反应"
        mode = None
        print("关闭绘图")
    elif key & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
