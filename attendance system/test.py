import cv2 as cv
import mysql.connector
from datetime import datetime


rec = cv.face.LBPHFaceRecognizer_create()
rec.read('trainingData.yml')

face_cs = cv.CascadeClassifier(cv.data.haarcascades + 'haarcascade_frontalface_default.xml')
cap = cv.VideoCapture(1)

names = {
    125: "Manabendu Karfa",
    129: "Asit Rajesh Wanjari",
    131 : "A Rana"
}

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="mk7riku23",
    database="attendance_system"
)
cursor = db.cursor()


logged_today = set()

while True:
    ret, frame = cap.read()
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    faces = face_cs.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in faces:
        id_, confidence = rec.predict(gray[y:y + h, x:x + w])

        if confidence < 74:
            now = datetime.now()
            today = now.strftime('%a').lower()
            day_column = today[:3]
            week_number = now.isocalendar()[1]

            cursor.execute("SELECT name FROM students WHERE id = %s", (id_,))
            result = cursor.fetchone()
            student_name = result[0] if result else "Unknown"

            label = f"ID: {id_}"
            name = f"Name: {student_name}"
            color = (0, 255, 110)

            if id_ not in logged_today:
                cursor.execute("""
                    SELECT log_id FROM attendance_log
                    WHERE student_id = %s AND week_number = %s
                """, (id_, week_number))
                record = cursor.fetchone()

                if record:
                    cursor.execute(f"""
                        UPDATE attendance_log
                        SET {day_column} = 'Present'
                        WHERE student_id = %s AND week_number = %s
                    """, (id_, week_number))
                else:
                    days = ['mon', 'tue', 'wed', 'thu', 'fri', 'sat']
                    day_data = {d: 'Present' if d == day_column else None for d in days}

                    cursor.execute(f"""
                        INSERT INTO attendance_log (
                            student_id, name, week_number,
                            mon, tue, wed, thu, fri, sat
                        ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
                    """, (
                        id_, student_name, week_number,
                        day_data['mon'], day_data['tue'], day_data['wed'],
                        day_data['thu'], day_data['fri'], day_data['sat']
                    ))

                db.commit()
                logged_today.add(id_)

        else:
            label = "Unknown"
            name = ""
            color = (0, 0, 255)

        cv.rectangle(frame, (x, y), (x + w, y + h), color, 2)
        cv.putText(frame, label, (x, y - 10), cv.FONT_HERSHEY_SIMPLEX, 0.9, color, 2)
        cv.putText(frame, name, (x, y + w + 30), cv.FONT_HERSHEY_SIMPLEX, 0.9, color, 2)

    cv.imshow("Face Recognition", frame)

    if cv.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv.destroyAllWindows()
cursor.close()
db.close()
