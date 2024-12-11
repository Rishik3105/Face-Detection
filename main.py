import cv2 as cv
import numpy as np
path=input('Give your image path')
img=cv.imread(path)
cv.imshow('Original Image',img)
gray_img=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('Gray Scale Image',gray_img)
haar_cascade=cv.CascadeClassifier('D:\Python\opeancv\haar_face.xml')
faces_rect=haar_cascade.detectMultiScale(gray_img,scaleFactor=1.1,minNeighbors=1)
print(f'number of faces found in the given image = {len(faces_rect)}')
for (x,y,w,h) in faces_rect:
    cv.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
cv.imshow('Detected Face',img)
cv.waitKey(0)

