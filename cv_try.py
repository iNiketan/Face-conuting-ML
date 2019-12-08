# this file will be used be used with opencv
# to solve the problem

import cv2
import numpy as np

cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

img = cv2.imread('img_data/10001.jpg') #image lacation
gray_img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
face = cascade.detectMultiScale(gray_img, 1.3, 5)
for (x,y,w,h) in face:
    cv2.rectangle(img,(x,y),(x+w, y+h), (255,0,0), 1)
    roi_gray = gray_img[y:y + h, x:x + w]
    roi_color = img[y:y + h, x:x + w]

cv2.imshow('imaga', img)
cv2.waitKey(0)
cv2.destroyAllWindows()





