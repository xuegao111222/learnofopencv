import cv2
import numpy as np
#有效数
cars = []
min_w = 90
min_h = 90
#检测线的高度
line_h = 700

offset = 2
carno = 0
def center(x,y,w,h):
   x1 = int(w/2)
   y1 = int(h/2)
   cx = x + x1
   cy = y + y1
   return cx,cy
cap = cv2.VideoCapture('d:\\shenfen\\video.mp4')

bgsubmog = cv2.bgsegm.createBackgroundSubtractorMOG()
#形态学kernel
kernel = cv2.getStructuringElement(cv2.MORPH_RECT,(5,5))


while True:
   ret,frame = cap.read()

   if(ret == True):
      #灰度化
      cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
      # print(frame.shape)

      #去噪(高斯)
      blur = cv2.GaussianBlur(frame,(3,3),5)
      #去背景
      mask = bgsubmog.apply(blur)

      #腐蚀
      erode = cv2.erode(mask,kernel)

      #膨胀 还原放大
      dilate = cv2.dilate(erode,kernel,iterations=3)

      #闭操作
      close = cv2.morphologyEx(dilate,cv2.MORPH_CLOSE,kernel,iterations=2)

      cnts,h =cv2.findContours(close,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

      cv2.line(frame,(10,line_h),(1200,line_h),(0,255,0),3)
      for (i,c) in enumerate(cnts):
         (x,y,w,h) = cv2.boundingRect(c)
         cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),2)
      #验证是否为有效车辆
         isValid = (w>=min_w) and (h>=min_h)
         if( not isValid):
            continue

         #到这里都是有效的车
         cpoint = center(x,y,w,h)
         cars.append(cpoint)


         for (x,y) in cars:
            if (line_h - offset) < y < (line_h + offset):
               carno += 1
               cars.remove((x,y))
               print(carno)
         cv2.imshow('frame',frame)
      # cv2.imshow('video',mask)
      # cv2.imshow('erode',erode)
      # cv2.imshow('dilate',dilate)
      # cv2.imshow('close',close)
      key = cv2.waitKey(1)
      if key == 27:
         break

cap.release()
cv2.destroyAllWindows()