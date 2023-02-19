import cv2 as cv
import time

face_cascade = cv.CascadeClassifier("D:\\Robotics\Projects\OpenCV-Projects\human-face-and-smile\haarcascade\face.xml")
smile_cascade = cv.CascadeClassifier("D:\\Robotics\Projects\OpenCV-Projects\human-face-and-smile\haarcascade\smile.xml")

video = cv.VideoCapture(0)
while True:
    check, frame = video.read()
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    face = face_cascade.detectMultiScale(gray, scaleFactor=1.01, minNeighbors=5)
    for x, y, w, h in face:
        smile = smile_cascade.detectMultiScale(gray, scaleFactor=1.01, minNeighbors=5)
        image = cv.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 3)
        for x, y, w, h in smile:
            image = cv.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 255), 3)
    cv.imshow("my image", frame)
    key = cv.waitKey(0)
    if key == ord("q"):
        break
cv.release()
cv.destroyAllWindows()