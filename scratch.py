import cv2
from pprint import pprint
cap = cv2.VideoCapture(0)
while True :
    # ret - получилось ли достать кадр
    # frame - сам кадр
    ret, frame = cap.read()
    print(frame.shape)
    height, width, _ = frame.shape
    frame [:100, :100] = [0,0,0]
    frame [height - 100:, width - 100:] = [0,0,0]
    frame [:100, width - 100:] = [0,0,0]
    frame [height - 100:, :100] = [0,0,0]
    frame [height // 2 - 100 // 2 :height//2+100//2,width//2 - 100//2 :width//2 + 100//2] = [0,0,0]

    cv2.imshow('camera',frame)
    key = cv2.waitKey(1000)
    # название окна , сам кадр
    for el in frame :
        for i in el:
            print(1,end="")
    print(key)
    if key == 32:
        break
    # ожидать нажатия
cv2.destroyALLWindows()
cap.release()


