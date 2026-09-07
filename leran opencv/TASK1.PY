import cv2
import numpy as np

start_pos = None
cur_pos = None         # 鼠标当前位置（实时预览用）
mode = None            # None / 'line' / 'circle' / 'rect'
drawing = False        # 是否正在拖拽

def draw_shape(canvas, p1, p2, m):
    """在 canvas 上按模式 m 画一个 p1 -> p2 的图形"""
    if m == 'line':
        cv2.line(canvas, p1, p2, (0, 0, 255), 2)
    elif m == 'circle':
        radius = int(np.sqrt((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2))
        cv2.circle(canvas, p1, radius, (255, 255, 0), 2)
    elif m == 'rect':
        cv2.rectangle(canvas, p1, p2, (0, 255, 0), 2)

def mouse_callback(event, x, y, flags, userdata):
    global start_pos, cur_pos, drawing
    cur_pos = (x, y)

    if mode is None:
        return

    if event == cv2.EVENT_LBUTTONDOWN:   # 按下：开始拖
        drawing = True
        start_pos = (x, y)
    elif event == cv2.EVENT_LBUTTONUP:   # 松开：定稿
        if drawing:
            draw_shape(img, start_pos, (x, y), mode)
            print(mode, "完成:", start_pos, "->", (x, y))
            drawing = False

cv2.namedWindow('img', cv2.WINDOW_NORMAL)
cv2.setMouseCallback('img', mouse_callback)
img = np.zeros((480, 640, 3), np.uint8)

while True:
    # 拖拽中显示带预览的临时图，否则显示正式画布
    if drawing:
        temp = img.copy()
        draw_shape(temp, start_pos, cur_pos, mode)
        cv2.imshow('img', temp)
    else:
        cv2.imshow('img', img)

    key = cv2.waitKey(10)

    if key & 0xFF == ord('l'):
        mode = 'line'
        print("划线模式（按住拖动）")
    elif key & 0xFF == ord('c'):
        mode = 'circle'
        print("画圆模式（按住拖动）")
    elif key & 0xFF == ord('r'):
        mode = 'rect'
        print("矩形模式（按住拖动）")
    elif key & 0xFF == ord('x'):
        mode = None
        print("关闭绘图")
    elif key & 0xFF == ord('q'):
        break
    elif key & 0xFF == ord('d'):
        img[:] = 0
        print('清除')
cv2.destroyAllWindows()
