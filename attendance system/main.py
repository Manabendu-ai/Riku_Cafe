import cv2 as cv

cap = cv.VideoCapture(1)
detector = cv.CascadeClassifier('haarcascade_frontalface_default.xml')

id = int(input("id: "))
sampleNums = 0
while True:
    ret, img = cap.read()
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    faces = detector.detectMultiScale(gray, 1.3, 5)
    for (x,y,w,h) in faces:
        cv.rectangle(img,(x,y), (x+w,y+h), (255,0,0),2)
        cv.imwrite(f"dataset/know_faces/user.{id}.{str(sampleNums)}.jpg", gray[y:y+h, x:x+w])
        sampleNums+=1
        cv.imshow('frames', img)

    if cv.waitKey(100) & 0xFF == ord('q'):
        break

cap.release()
cv.destroyAllWindows()