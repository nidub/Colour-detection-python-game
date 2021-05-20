import cv2
import pyautogui
import numpy as np
import keyboard

def rundino():
    #print("Dino game started")
    blueLowerBound = np.array([94, 80, 2])
    blueUpperBound = np.array([128,255,255])

    greenLowerBound = np.array([25, 52, 72], np.uint8)
    greenUpperBound = np.array([102, 255, 255], np.uint8)

    kernelOpen=np.ones((5,5))
    kernelClose=np.ones((20,20))

    cap= cv2.VideoCapture(0, cv2.CAP_DSHOW)

    cap.set(cv2.CAP_PROP_FRAME_WIDTH,360)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT,240)

    while True:

        _, frame=cap.read()
        
        frameHSV= cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

        # Set range for blue color and define mask
        blueMask=cv2.inRange(frameHSV,blueLowerBound,blueUpperBound)

        # Set range for green color and define mask
        greenMask = cv2.inRange(frameHSV, greenLowerBound, greenUpperBound)

        # For blue
        blueMaskOpen=cv2.morphologyEx(blueMask,cv2.MORPH_OPEN,kernelOpen)
        blueMaskClose=cv2.morphologyEx(blueMaskOpen,cv2.MORPH_CLOSE,kernelClose)

        blueMaskFinal=blueMaskClose
        blueCount,_=cv2.findContours(blueMaskFinal.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)

        # For green
        greenMaskOpen=cv2.morphologyEx(greenMask,cv2.MORPH_OPEN,kernelOpen)
        greenMaskClose=cv2.morphologyEx(greenMaskOpen,cv2.MORPH_CLOSE,kernelClose)

        greenMaskFinal=greenMaskClose
        greenCount,_=cv2.findContours(greenMaskFinal.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
        
        # cv2.imshow("OutputGreen", greenMaskFinal)
        # cv2.imshow("OutputBlue", blueMaskFinal)
        # cv2.imshow("original", frame)
        # if cv2.waitKey(1) & 0xFF == ord('q'):
        #     break

        if len(blueCount)==1:
            #pyautogui.press('space') 
            print("blue detected")
        if len(greenCount)==1:
            #pyautogui.press('space') 
            print("green detected")
        if keyboard.is_pressed('Esc') == True:
            break
    
    cap.release()
    cv2.destroyAllWindows()    
