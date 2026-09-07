import cv2
import numpy as np

start_pos = None
cur_pos = None         # 鼠标当前位置（矩形实时预览用）
mode = None            # None / 'line' / 'circle' / 'rect'
drawing = False        # 是否正在拖拽（矩形）

def mouse_callback(event, x, y, flags, userdata):
    global start_pos, cur_pos, drawing
    cur_pos = (x, y)

    # 矩形模式：按住拖动，实时预览，松开定稿
    if mode == 'rect':
        if event == cv2.EVENT_LBUTTONDOWN:
            drawing = True
            start_pos = (x, y)
        elif event == cv2.EVENT_LBUTTONUP:
            if drawing:
                cv2.rectangle(img, start_pos, (x, y), (0, 255, 0), 2)
                print("矩形:", start_pos, "->", (x, y))
                drawing = False
        return

    # 线/圆模式：点两下画
    if mode is None or event != cv2.EVENT_LBUTTONDOWN:
        return

    if start_pos is None:          # 第一次点：存起点
        start_pos = (x, y)
        return

    if mode == 'line':             # 第二次点：画线
        cv2.line(img, start_pos, (x, y), (0, 0, 255), 2)
        print("划线:", start_pos, "->", (x, y))
    elif mode == 'circle':         # 第二次点：画圆
        radius = int(np.sqrt((x - start_pos[0])**2 + (y - start_pos[1])**2))
        cv2.circle(img, start_pos, radius, (255, 255, 0), 2)
        print("画圆: 圆心", start_pos, "半径", radius)
    start_pos = None

cv2.namedWindow('img', cv2.WINDOW_NORMAL)
cv2.setMouseCallback('img', mouse_callback)
img = np.zeros((480, 640, 3), np.uint8)

while True:
    # 矩形拖拽时显示带预览的临时图，否则显示正式画布
    if mode == 'rect' and drawing:
        temp = img.copy()
        cv2.rectangle(temp, start_pos, cur_pos, (0, 255, 0), 2)
        cv2.imshow('img', temp)
    else:
        cv2.imshow('img', img)

    key = cv2.waitKey(10)

    if key & 0xFF == ord('l'):
        mode = 'line'
        print("划线模式")
    elif key & 0xFF == ord('c'):
        mode = 'circle'
        print("画圆模式")
    elif key & 0xFF == ord('r'):
        mode = 'rect'
        print("矩形模式（按住拖动）")
    elif key & 0xFF == ord('x'):
        mode = None
        print("关闭绘图")
    elif key & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
