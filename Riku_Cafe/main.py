import cv2 as cv
import os
from cvzone.HandTrackingModule import HandDetector

cap = cv.VideoCapture(1)

bg = cv.imread("bg.png")

menuPath = ["Resources/Modes/1.png","Resources/Modes/2.png",
            "Resources/Modes/3.png","Resources/Modes/4.png"]

menuImgs = []
counterPause = 0

for paths in menuPath:
    menuImgs.append(cv.imread(paths))

modeType = 0

detector = HandDetector(detectionCon = 0.8, maxHands = 1)

selection = -1
counter = 0
end = False
modePositions = [(1136, 196), (1000, 384), (1136, 581)]
selectionSpeed = 7

icons = []

for i in range(1,10):
    icons.append(cv.imread(f"Resources/Icons/{i}.png"))

selectionList =[-1,-1,-1]

while True:
    ret, img = cap.read()

    hands,img = detector.findHands(img)
    bg[139:139 + 480, 50:50 + 640] = img
    bg[0:720, 847: 1280] = menuImgs[modeType]
    if hands and counterPause==0 and modeType<3:
        hand1 = hands[0]
        fingers = detector.fingersUp(hand1)
        print(fingers)

        if fingers == [0,1,0,0,0]:
            if selection != 1:
                counter = 1

            selection = 1
        elif fingers == [0,1,1,0,0]:
            if selection != 2:
                counter = 1
            selection = 2

        elif fingers == [0,1,1,1,0]:
            if selection != 3:
                counter = 1
            selection = 3

        else:
            selection -=1
            counter = 0

        if counter>0:
            counter+=1
            cv.ellipse(
                bg,
                modePositions[selection-1],
                (103, 103), 0, 0,
                counter * selectionSpeed, (0, 255, 0), 20
            )

            if counter*selectionSpeed>360:
                selectionList[modeType] = selection
                modeType+=1
                counter = 0
                selection = -1
                counterPause = 1

    if counterPause>0:
        counterPause+=1
        if counterPause>60:
            counterPause = 0

    if selectionList[0] != -1:
        bg[636:636+65, 133:133+65] = icons[selectionList[0]-1]
    if selectionList[1] != -1:
        bg[636:636 + 65, 340:340 + 65] = icons[2+selectionList[1]]
    if selectionList[2] != -1:
        bg[636:636 + 65, 542:542 + 65] = icons[5+selectionList[2]]

    cv.imshow("Riku's Cafe", bg)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv.destroyAllWindows()