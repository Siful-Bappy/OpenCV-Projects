import cv2 as cv
video = cv.VideoCapture(0)

while True:
    ret, img = video.read()
    cv.imshow("Frame", img)
    k = cv.waitKey(1)
    if(k==ord("q")):
        break
video.release()
cv.destroyAllWindows()
