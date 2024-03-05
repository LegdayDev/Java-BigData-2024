# file: p63_openCV.py
# desc: OpenCV 영상 처리 - 동영상 불러오기, 캡쳐, 편집

import cv2

samplePath = "./resources/earthVideo.mp4"
cam = cv2.VideoCapture(samplePath)  # 0 은 웹캠 또는 동영상 경로

while True:
    ret, frame = cam.read()

    if not ret:
        cam = cv2.VideoCapture(samplePath)
        continue

    ## 영상 편집
    blur = cv2.blur(frame, (5, 5))
    flip = cv2.flip(frame, 0)

    cv2.imshow("original video", frame)  # 원본
    cv2.imshow("blur video", blur) # 블러
    cv2.imshow("flip video", flip) # 뒤집기

    key = cv2.waitKey(5)  # 5ms

    if key == ord("q"):  # ord('q') = q버튼 , 27 = ESC 버튼
        break
    elif key == ord("c"):  # c 버튼 누르면 캡쳐
        cv2.imwrite("./images/day09Img/capt.jpg", frame)

cam.release()
cv2.destroyAllWindows()
