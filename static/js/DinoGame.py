import cv2
import pyautogui
import numpy as np

def rundino():
    lowerBound=np.array([71,112,112])
    upperBound=np.array([128,255,255])

    kernelOpen=np.ones((5,5))
    kernelClose=np.ones((20,20))

    cap= cv2.VideoCapture(0)

    cap.set(cv2.CAP_PROP_FRAME_WIDTH,360)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT,240)

    while True:

        _, frame=cap.read()
        
        frameHSV= cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

        mask=cv2.inRange(frameHSV,lowerBound,upperBound)

        maskOpen=cv2.morphologyEx(mask,cv2.MORPH_OPEN,kernelOpen)
        maskClose=cv2.morphologyEx(maskOpen,cv2.MORPH_CLOSE,kernelClose)

        maskFinal=maskClose
        count,_=cv2.findContours(maskFinal.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)

        if len(count)==1:
            pyautogui.press('space') 
    
    cap.release()
    cv2.destroyAllWindows()    

rundino()

