import cv2
import numpy as np

dispW = 192
dispH = 108
frame_rate = 10
flip = 2

camSet='nvarguscamerasrc ! video/x-raw(memory:NVMM), width=1920, height=1080, format=NV12,framerate='+str(frame_rate)+'/1 ! nvvidconv flip-method='+str(flip)+' ! video/x-raw, width='+str(dispW)+',height='+str(dispH)+', format=BGRx ! videoconvert ! video/x-raw, format=BGR ! appsink' 


camera = cv2.VideoCapture(camSet)

img_itr = 0
while True:
    ret, frame = camera.read()

    cv2.imshow('cam', frame)
    cv2.imwrite('images/'+str(img_itr)+'img.png', frame)

    if cv2.waitKey(1)==ord('q'):
         break

    img_itr += 1


camera.release()
cv2.destroyAllwindows()






