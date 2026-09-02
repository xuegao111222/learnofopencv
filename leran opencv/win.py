import cv2

cv2.namedWindow('new',cv2.WINDOW_NORMAL)
cv2.resizeWindow('new',340,280)
cv2.imshow('new',0)
key = cv2.waitKey(0) 
if(key == 'q'):
    exit()
cv2.destroyAllWindows()
