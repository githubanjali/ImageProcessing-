# -*- coding: utf-8 -*-
"""
Created on Sat Apr  6 14:11:43 2019

@author: Anjali
"""

import numpy as np
import cv2

def sketch(image):
    img_gray = cv2.cvtcolor(image,cv2.BGR2GRAY)
    img_gray_blur = cv2.GussianBlur(img_gray,(5,5),0)
    canny_edge = cv2.Canny(img_gray_blur,10,70)
    ret,mask = cv2.threshold(canny_edge, 70 , 255, cv2.THRESH_BINARY_INV)

cap = cv2.VideoCapture(0)    

while True:
    ret,frame = cap.read()
    cv2.imshow('Live Video', sketch(frame))
    if cv2.waitkey(1) == 13:
        break;
    
    