### doc for haarcascate-> https://github.com/opencv/opencv/blob/master/data/haarcascades/haarcascade_frontalcatface_extended.xml
import cv2 as cv
face_cascade=cv.CascadeClassifier("D:\\Robotics\Projects\OpenCV-Projects\cat-face-recognition\cat_face.xml")
image_name = "cat_01.jpg"
img = cv.imread("D:\\Robotics\Projects\OpenCV-Projects\cat-face-recognition\images\cat_01.jpg")
img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(img_gray, scaleFactor=1.01, minNeighbors=5)
# print(faces)

for x, y, w, h in faces:
    image = cv.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 3)
cv.imshow("Cat", img)
cv.waitKey(0)
cv.destroyAllWindows()