
import cv2

#webcam capture
cap = cv2.VideoCapture(0)
facerec = cv2.CascadeClassifier('recursos/haarcascade_frontalface_alt.xml')
eyerec = cv2.CascadeClassifier('recursos/haarcascade_eye.xml')
#smilerec = cv2.CascadeClassifier('recursos/haarcascade_smile.xml')

while(True):
    ret, frame = cap.read()

    #gray scale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    face = facerec.detectMultiScale(gray, 1.3, 5)
    eye = eyerec.detectMultiScale(gray, 1.3, 5)
    #smile = smilerec.detectMultiScale(gray, 1.3, 5)

    #Rectangle
    for (x, y, w, h) in face:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

    for (x, y, w, h) in eye:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)

    for (x, y, w, h) in body:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)


    #Display
    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()