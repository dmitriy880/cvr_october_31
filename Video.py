import cv2
from pprint import pprint
import sys
cap = cv2.VideoCapture(0)
while True :
    # ret - получилось ли достать кадр
    # frame - сам кадр
    ret, frame = cap.read()
    # название окна , сам кадр
    print(ret)
    for el in frame :
        for i in el:
            print(1,end="")
    cv2.imshow('camera',frame)
    cv2.waitKey(1)
    # ожидать нажатия