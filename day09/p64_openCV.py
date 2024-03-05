# file: p64_openCV.py
# desc: OpenCV 영상 처리 - 영상에서 얼굴 검출

import cv2

samplePath = "./resources/news.mp4"
faceCascade = cv2.CascadeClassifier("./day09/haarcascade_frontalface_default.xml")
cam = cv2.VideoCapture(samplePath)

while True:
    ret, frame = cam.read()

    if not ret:
        cam = cv2.VideoCapture(samplePath)
        continue

    ## 영상에서 얼굴 검출
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(
        gray, scaleFactor=1.2, minNeighbors=5, minSize=(20, 20)
    )

    for x, y, w, h in faces:
        cv2.rectangle(
            frame, pt1=(x, y), pt2=(x + w, y + h), color=(0, 0, 255),thickness=2
        )


    cv2.imshow("original video", frame)

    key = cv2.waitKey(5)
    if key == ord("q"):
        break

cam.release()
cv2.destroyAllWindows()
