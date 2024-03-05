# file: p59_openCV.py
# desc: OpenCV - 흑백, x축y축으로 자르기, 크기변경

# OpenCV(Open Computer Vision) : 실시간 이미지 프로세싱 라이브러리
# 명령어 >> pip3 install opencv-python

import cv2

# print(cv2.__version__)

#  cv2.IMREAD_UNCHANGED -> 디폴트(아무것도 하지마)
#  cv2.IMREAD_GRAYSCALE -> 컬러이미지를 흑백이미지로 변환
image = cv2.imread("./images/day09Img/ronaldo.png", cv2.IMREAD_UNCHANGED)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # 원본을 흑백으로 변경

height, width, channel = image.shape
print(height, width, channel)

sizeSmall = cv2.resize(image, (width // 2, height // 2))

img_cropped = image[: (height // 2), : (width // 2)]  # y축 반, x축 반 자르기

cv2.imshow("CR7 is King, color", image)  # 원본
cv2.imshow("Reduced CR7", sizeSmall)  # 반으로 줄인 사진
cv2.imshow("CR7 is King, gray", gray)  # 흑백
cv2.imshow("CR7 Half", img_cropped)
cv2.waitKey(0)
cv2.destroyAllWindows()
