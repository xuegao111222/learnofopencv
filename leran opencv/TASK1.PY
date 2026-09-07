import cv2
import numpy as np

start_pos = None
draw_line = False
draw_circle = False
def mouse_callback_l(event,x,y,flags,userdata):
    global start_pos
    if not draw_line and not draw_circle:
         return
    if event == cv2.EVENT_LBUTTONDOWN and draw_line:
        if start_pos is None:
            start_pos = (x,y)
        else: 
            cv2.line(img,start_pos,(x,y),(0,0,255),2)
            print("划线:",start_pos,"->",(x,y))
            start_pos = None
    #画圆逻辑        
    elif draw_circle and  event == cv2.EVENT_LBUTTONDOWN :
         if start_pos is None:
              start_pos=(x,y)
         else: 
              radius = int(np.sqrt((x-start_pos[0])**2+(y-start_pos[1])**2))
              cv2.circle(img,start_pos,radius,(255,255,0))
              start_pos = None

cv2.namedWindow('img',cv2.WINDOW_NORMAL)
cv2.setMouseCallback('img',mouse_callback_l)
img = np.zeros((480,640,3),np.uint8)

while True:
    cv2.imshow('img',img)
    key = cv2.waitKey(10)

    if key & 0xFF == ord('l'):
        draw_line = not draw_line
        print('划线启动')

    if key & 0xFF == ord('c'):
        draw_circle = not draw_circle
        print('画圆启动')
    if key & 0xFF == ord('q'):
            break
cv2.destroyAllWindows()