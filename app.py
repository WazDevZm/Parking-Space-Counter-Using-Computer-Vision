#Project created by Wazingwa Mugala
#Computer Engineering@CBU
import cv2
import mediapipe as mp
import numpy as np
import time
import pandas as pd
import pickle


width = 107
height = 48

try:
    with open('CarParkPos', 'rb') as f:
        posList = pickle.load(f)
except:
    posList = []
    
def mouseClick(events, x, y, flags, params):
    if events == cv2.EVENT_FLAG_LBUTTON:
        posList.append((x,y))
    if events == cv2.EVENT_FLAG_RBUTTON:
        for i, pos in enumerate(posList):
            x1, y1 = pos
            if x1 < x < x1 + width and y1 < y < y1 + height:
                posList.pop(i)
    with open('CarParkPos', 'wb') as f:
        pickle.dump(posList,f)

while True:
    img = cv2.imread('carParkImg.png')
    for pos in posList:
        cv2.rectangle(img, pos, (pos[0] + width, pos[1] + height), (255, 0 , 255), 2)
    cv2.imshow("CarParkLiveFeed", img)
    cv2.setMouseCallback("Image", mouseClick)
    cv2.waitKey(1)