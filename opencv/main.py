import cv2 as cv
import numpy as np


cap = cv.VideoCapture(0)

while True:
    ret, img = cap.read()

    cv.imshow("recording", img)
    if cv.waitKey(0) & 0xFF == ord('q'):
        break

cap.release()
cv.destroyAllWindows()