# file: p61_openCV.py
# desc: OpenCV 이미지 처리 계속 - 블러처리, 엣지검출, 외곽선 검출

import cv2

image = cv2.imread("./images/day09Img/ronaldo.jpg", cv2.IMREAD_UNCHANGED)

# 2번째 파라미터인 kSize 를 늘릴수록 블러처리가 강해진다.
dst = cv2.blur(image, (10, 10), anchor=(-1, -1), borderType=cv2.BORDER_DEFAULT)

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
sobel = cv2.Sobel(gray, cv2.CV_8U, 1, 0, 3)
laplacian = cv2.Laplacian(gray, cv2.CV_8U, ksize=3)
canny = cv2.Canny(image, 100, 255)

height, width, channel = image.shape

cv2.imshow("Original CR7", image)  # 원본
cv2.imshow("Blur CR7", dst)  # 블러처리
cv2.imshow("Sobel CR7", sobel)  # 입체감 있는 윤곽
cv2.imshow("Laplacian CR7", laplacian)  # 일반적인 윤곽 검출
cv2.imshow("Canny CR7", canny)  # 흑백으로 윤곽

cv2.waitKey(0)
cv2.destroyAllWindows()
