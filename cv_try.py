# this file will be used be used with opencv
# to solve the problem

import cv2
import os
#import numpy as np

os.chdir('/home/niketan/PycharmProjects/Face-conuting-ML')
cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

img = cv2.imread('image_data/10001.jpg') #image lacation
gray_img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
face = cascade.detectMultiScale(gray_img, 1.05, 5)
eyes = eye_cascade.detectMultiScale(gray_img, 1.05, 5)
for (x,y,w,h) in face:

    cv2.rectangle(img,(x,y),(x+w, y+h), (0,255,0), 3)

resize = cv2.resize(img,(600,600))

cv2.imshow('imaga', resize)
cv2.waitKey(0)
cv2.destroyAllWindows()





