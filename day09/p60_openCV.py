# file: p60_opencv.py
# desc: OpenCV - 뒤집기, 회전, 컬러반전, 이진화

import cv2

image = cv2.imread("./images/day09Img/ronaldo.jpg", cv2.IMREAD_UNCHANGED)
dst = cv2.flip(image, 0)  # 0은 위아래 반전, 1은 좌우반전

"""
채널은 R(Red), G(Green), B(Blue) 와 추가적으로 Alpha(투명도) 가 있다.
3채널은 Color 다.
"""

height, width, channel = image.shape
matrix = cv2.getRotationMatrix2D((width / 2, height / 2), 270, 0.6)
thrd = cv2.warpAffine(image, matrix, (width, height))
reverse = cv2.bitwise_not(image)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
ret, bny = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY)  

cv2.imshow("Original CR7", image)  # 원본
cv2.imshow("Flip CR7", dst)  # 뒤집기
cv2.imshow("Rotation CR7", thrd)  # 회전
cv2.imshow("Reverse CR7", reverse)  # 컬러반전
cv2.imshow("Gray CR7", gray)  # 흑백
cv2.imshow("Binary CR7", bny)  # 이진화(물체인식 할 때 사용)
cv2.waitKey(0)
cv2.destroyAllWindows()
